# model_provider_cli/client.py

import aiohttp
import json
from typing import Any, AsyncGenerator, Dict, List, Optional, Union

from .config import load_config
from .utils import Provider, Capability
from .exceptions import *

class APIClient:
  """
  APIClient – класс для обращения к API-серверу, предоставляющему
  функционал генерации текста, создания изображений, обработки аудио и голосового синтеза.

  Атрибуты:
   base_url (str): Базовый URL API-сервера.
   auth (Optional[tuple[str, str]]): Пара основной аутентификации.
   session (Optional[aiohttp.ClientSession]): HTTP-сессия для запросов.
  """
  
  def __init__(
    self,
    base_url: Optional[str] = None,
    auth: Optional[tuple] = None,
    config_path: Optional[str] = None
  ) -> None:
    """
    Инициализирует клиента, подгружая конфигурацию по умолчанию, из окружения или из файла.

    Args:
     base_url (Optional[str]): Базовый URL сервера; если не указан, берется из конфигурации.
     auth (Optional[tuple[str, str]]): Данные для базовой аутентификации (логин, пароль).
     config_path (Optional[str]): Путь к файлу конфигурации.
    """
    config = load_config(config_path)
    self.base_url: str = (base_url or config.get("base_url", "http://localhost:8000")).rstrip("/")
    self.auth: Optional[tuple] = auth or config.get("auth")
    self.session: Optional[aiohttp.ClientSession] = None

  async def _get_session(self) -> aiohttp.ClientSession:
    """
    Создает или возвращает уже существующую aiohttp-сессию.

    Returns:
     aiohttp.ClientSession: Сессия для выполнения HTTP-запросов.
    """
    if self.session is None or self.session.closed:
      self.session = aiohttp.ClientSession()
    return self.session

  async def close(self) -> None:
    """
    Закрывает HTTP-сессию.
    """
    if self.session is not None:
      await self.session.close()

  def __init__(self, base_url: str, auth: Optional[tuple] = None) -> None:
    self.base_url: str = base_url.rstrip("/")
    self.auth: Optional[tuple] = auth
    self.session: Optional[aiohttp.ClientSession] = None

  async def _get_session(self) -> aiohttp.ClientSession:
    if self.session is None or self.session.closed:
      self.session = aiohttp.ClientSession()
    return self.session

  async def close(self) -> None:
    """Закрывает сессию aiohttp."""
    if self.session is not None:
      await self.session.close()

  async def _send_request(
    self,
    endpoint: str,
    method: str = "POST",
    json_data: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
    files: Optional[Dict[str, Any]] = None,
    stream: bool = False,
  ) -> aiohttp.ClientResponse:
    """
    Внутренняя функция для отправки HTTP-запроса.

    Args:
     endpoint (str): Конечная точка API (например, "/text").
     method (str): HTTP-метод ("GET", "POST", и т.д.).
     json_data (Optional[Dict[str, Any]]): JSON-данные запроса.
     data (Optional[Dict[str, Any]]): Данные формы.
     files (Optional[Dict[str, Any]]): Файлы для multipart-запроса.
     stream (bool): Флаг для обработки потокового ответа.

    Returns:
     aiohttp.ClientResponse: Ответ сервера.
     
    Raises:
     aiohttp.ClientResponseError: При ошибке HTTP-запроса.
    """
    url: str = f"{self.base_url}{endpoint}"
    session: aiohttp.ClientSession = await self._get_session()
    headers: Dict[str, str] = {}
    if json_data:
        headers["Content-Type"] = "application/json"
    auth: Optional[aiohttp.BasicAuth] = aiohttp.BasicAuth(*self.auth) if self.auth else None

    if files:
        # Для передачи файлов используем FormData (multipart/form-data)
        form = aiohttp.FormData()
        if data:
            for key, value in data.items():
                form.add_field(key, str(value))
        for key, file_tuple in files.items():
            # file_tuple: (filename, file_bytes, content_type)
            filename, file_bytes, content_type = file_tuple
            form.add_field(key, file_bytes, filename=filename, content_type=content_type)
        response: aiohttp.ClientResponse = await session.request(method, url, data=form, auth=auth, headers=headers, allow_redirects=False)
    else:
        response = await session.request(method, url, json=json_data, data=data, auth=auth, headers=headers)
    response.raise_for_status()
    return response
      
  async def generate_text(
    self,
    message: str,
    provider: Provider,
    model: Optional[str] = None,
    image_bytes: Optional[Union[str, bytes]] = None, # новый параметр для изображения
    max_tokens: int = 150,
    temperature: float = 0.7,
    stream: bool = False,
    system: Optional[str] = None,
    messages: Optional[List[Dict[str, Any]]] = None,
    reasoning_effort: Optional[str] = None,
  ) -> Union[str, AsyncGenerator[str, None]]:
    """
    Генерирует текст с использованием заданного провайдера.

    Args:
      message (str): Основное текстовое сообщение.
      provider (str): Имя провайдера (например, "openai", "gemini").
      model (Optional[str]): Имя модели (если требуется).
      max_tokens (int): Максимальное число токенов.
      temperature (float): Параметр температуры генерации.
      stream (bool): Если True – возвращает асинхронный генератор для потокового ответа.
      system (Optional[str]): Системное (инструкционное) сообщение.
      messages (Optional[List[Dict[str, Any]]]): Дополнительный контекст.
      reasoning_effort (Optional[str]): Параметр для режима рассуждения.
      image_bytes (Optional[Union[str, bytes]]): Байты изображения или строка в формате base64 для передачи визуальной информации.

    Returns:
     Union[str, AsyncGenerator[str, None]]: Сгенерированный текст или генератор чанков.

    Raises:
     ValueError: Если передан некорректный тип image_bytes или неверный Provider.
    """
    if not isinstance(provider, Provider):
      raise ValueError("Неверный провайдер. Используйте один из: " + ", ".join(p.value for p in Provider))
    payload: Dict[str, Any] = {
      "message": message,
      "provider": provider.value,
      "model": model,
      "max_tokens": max_tokens,
      "temperature": temperature,
      "stream": stream,
      "system": system or "",
      "messages": messages or [],
      "reasoning_effort": reasoning_effort,
    }
  # Если передано изображение, конвертируем его в base64-строку
    if image_bytes is not None:
      import base64
      if isinstance(image_bytes, bytes):
          payload["image_bytes"] = base64.b64encode(image_bytes).decode("utf-8")
      elif isinstance(image_bytes, str):
          payload["image_bytes"] = image_bytes
      else:
          raise ValueError("Параметр image_bytes должен быть типа bytes или str")
        
    response = await self._send_request("/text", json_data=payload, stream=stream)
    if stream:
      async def text_stream() -> AsyncGenerator[str, None]:
        async for line in response.content:
          chunk: str = line.decode("utf-8")
          if chunk:
            yield chunk
          
      return text_stream()
    else:
      data = await response.json()
      # Ожидается ключ с результатом ответа (например, "result")
      return data.get("result") or data.get("generated_text") or str(data)

  async def generate_image(
    self,
    prompt: str,
    provider: Provider,
    model: Optional[str] = None,
    size: str = "1024x1024"
  ) -> Dict[str, Any]:
    """
    Генерирует изображение по описанию.

    Args:
     prompt (str): Текстовое описание для генерации изображения.
     provider (Provider): Провайдер для генерации изображений.
     model (Optional[str]): Название модели (если требуется).
     size (str): Размер изображения (например, "1024x1024").

    Returns:
     Dict[str, Any]: Результат генерации (например, URL картинки).

    Raises:
     ProviderNotImplementedError: Если провайдер не реализован.
     AuthenticationError: При ошибке аутентификации.
     ServerError: При ошибке на стороне сервера.
    """
    payload: Dict[str, Any] = {
      "prompt": prompt,
      "provider": provider.value,
      "model": model or "",
      "size": size,
    }
    try:
        response = await self._send_request("/image", json_data=payload)
        return await response.json()
    except NotImplementedError as e:
        raise ProviderNotImplementedError(str(e)) from e  # Перехватываем и выбрасываем свое
    except aiohttp.ClientResponseError as e:  # Добавлено для единообразия обработки ошибок
        if e.status == 401:
            raise AuthenticationError("Authentication failed") from e
        elif e.status == 404:
            raise APIClientError(f"Not found: {e.message}") from e # Обработаем 404
        else:
            raise ServerError(f"Server error: {e.status} - {e.message}") from e

  async def process_audio(
    self,
    audio_file: bytes,
    provider: Provider,
    mode: Optional[str] = None,
    format_output: str = "text",
    async_process: bool = False,
    transcriptions: Optional[Dict[str, Any]] = None,
  ) -> str:
    """
    Обрабатывает аудио (например, транскрибацию).

    Args:
     audio_file (bytes): Байты аудиофайла.
     provider (Provider): Провайдер для обработки аудио.
     mode (Optional[str]): Режим обработки.
     format_output (str): Формат вывода ("text" или "json").
     async_process (bool): Флаг асинхронной обработки.
     transcriptions (Optional[Dict[str, Any]]): Дополнительные параметры транскрипции.

    Returns:
     str: Транскрибированный текст или иные данные.
    """
    data: Dict[str, Any] = {
      "provider": provider.value,
      "mode": mode or "",
      "format_output": format_output,
      "async_process": async_process,
      "transcriptions": json.dumps(transcriptions or {}),
    }
    files: Dict[str, Any] = {
      "audio_file": ("audio.mp3", audio_file, "audio/mpeg")
    }
    response = await self._send_request("/audio/", data=data, files=files)
    data_response = await response.json()
    return data_response.get("transcription", str(data_response))

  async def generate_voice(
    self,
    text: str,
    provider: Provider,
    model: Optional[str] = None
  ) -> Dict[str, Any]:
    """
    Выполняет синтез речи (TTS) по заданному тексту.

    Args:
     text (str): Исходный текст для озвучивания.
     provider (Provider): Провайдер для голосового синтеза.
     model (Optional[str]): Название модели (если требуется).

    Returns:
     Dict[str, Any]: Результаты TTS (например, аудио в формате base64).
    """
    payload: Dict[str, Any] = {
      "text": text,
      "provider": provider.value,
      "model": model or "",
    }
    response = await self._send_request("/voice", json_data=payload)
    return await response.json()

  async def get_available_models(
    self,
    provider: Optional[Union[Provider, str]] = None,
    capability: Optional[Union[Capability, str]] = None
  ) -> Dict[str, Any]:
    """
    Возвращает список доступных моделей по провайдеру и функциональности.

    Args:
     provider (Optional[Union[Provider, str]]): Имя провайдера.
     capability (Optional[Union[Capability, str]]): Тип возможностей (например, "text", "vision" и т.д.).

    Returns:
     Dict[str, Any]: Словарь с данными моделей.
    """
    if isinstance(provider, Provider):
      provider_value = provider.value
    else:
      provider_value = provider or ""
    if isinstance(capability, Capability):
      cap_value = capability.value
    else:
      cap_value = capability or ""
    payload: Dict[str, Any] = {"provider": provider_value, "capability": cap_value}
    response = await self._send_request("/models", json_data=payload)
    return await response.json()