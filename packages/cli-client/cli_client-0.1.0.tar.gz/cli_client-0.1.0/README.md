# CLI Client для Model Provider API

**CLI Client** – это асинхронная библиотека для взаимодействия с API-сервером, предоставляющим расширенный функционал:
  
• Генерация текстов  
• Создание изображений  
• Транскрибация аудио  
• Синтез речи  
• Получение доступных моделей по провайдеру и типу возможности

Библиотека позволяет использовать как синхронный, так и потоковый (streaming) режим работы через HTTP (aiohttp). Кроме того, она уже интегрирована с консольной утилитой, позволяющей вызывать основные функции напрямую из терминала.

------------------------------------------------------------
## Требования и установка

Для работы клиента необходим Python 3.8+ и следующие зависимости:

- asyncio
- aiohttp (для HTTP-запросов)
- (для разработки/тестирования) pytest, pytest-asyncio

Установку библиотеки из PyPI можно выполнить командой:
```
pip install cli-client
```
Если вы разрабатываете локально, установите зависимости через pip:
```
pip install aiohttp pytest pytest-asyncio
```
------------------------------------------------------------
## Быстрый старт

Ниже приведён пример базового использования клиента:
```
import asyncio
from cli_client import APIClient, Provider

async def main():
    # Инициализация клиента с указанием базового URL сервера
    client = APIClient(base_url="http://your-api-server:8000")
    
    # Пример генерации текста
    result_text = await client.generate_text(
        message="Привет, расскажи анекдот",
        provider=Provider.OPENAI
    )
    print("Сгенерированный текст:", result_text)
    
    # Пример генерации изображения
    result_image = await client.generate_image(
        prompt="A futuristic cityscape",
        provider=Provider.OPENAI,
        size="1024x1024"
    )
    print("Результат генерации изображения:", result_image)
    
    # Пример транскрибации аудио (файл читается как бинарные данные)
    with open("audio_sample.mp3", "rb") as f:
        audio_data = f.read()
    transcription = await client.process_audio(
        audio_file=audio_data,
        provider=Provider.OPENAI,
        format_output="json"
    )
    print("Результат транскрипции аудио:", transcription)
    
    # Пример синтеза речи
    voice_result = await client.generate_voice(
        text="Привет, как дела?",
        provider=Provider.OPENAI
    )
    print("Результаты синтеза речи:", voice_result)
    
    # Пример получения доступных моделей для текстовой генерации
    models = await client.get_available_models(provider=Provider.OPENAI, capability="text")
    print("Доступные модели для текста:", models)
    
    await client.close()

asyncio.run(main())
```
Также клиент можно запускать через консольную утилиту:
```
cli-client --ip http://localhost:8000 --provider openai --endpoint text --message "Привет, расскажи анекдот"
```
------------------------------------------------------------
## Основные функции и их возможности

### 1. Генерация текста – generate_text

Функция позволяет получить сгенерированный текст с учетом дополнительных параметров. При необходимости можно передать изображение в виде байтов или base64-строки для создания контекста.

**Параметры:**
- **message** (str): Основной текст запроса.
- **provider** (Provider): Провайдер генерации (например, OPENAI, GEMINI и др.).
- **model** (Optional[str]): Название модели, если требуется.
- **image_bytes** (Optional[Union[bytes, str]]): Байты изображения или base64-строка.
- **max_tokens** (int): Максимальное число токенов (по умолчанию 150).
- **temperature** (float): Параметр «тёплоты» генерации (по умолчанию 0.7).
- **stream** (bool): Если True, функция возвращает асинхронный генератор для потокового вывода.

**Пример использования:**
```
result = await client.generate_text(
    message="Расскажи интересную историю",
    provider=Provider.ANTHROPIC,
    max_tokens=300
)
print(result)
```
------------------------------------------------------------
### 2. Генерация изображения – generate_image

Функция отправляет текстовое описание (prompt) и возвращает сгенерированное изображение (например, URL).

**Параметры:**
- **prompt** (str): Описание изображения.
- **provider** (Provider): Провайдер генерации изображений.
- **model** (Optional[str]): Название модели (если требуется).
- **size** (str): Размер изображения (например, "1024x1024").

**Пример использования:**
```
result = await client.generate_image(
    prompt="A serene landscape with mountains",
    provider=Provider.OPENAI
)
print(result)
```
------------------------------------------------------------
### 3. Обработка аудио – process_audio

Позволяет передать аудиофайл для транскрибации (распознавания речи).

**Параметры:**
- **audio_file** (bytes): Байты аудиофайла.
- **provider** (Provider): Провайдер обработки аудио.
- **mode** (Optional[str]): Режим обработки (если имеется несколько).
- **format_output** (str): Формат вывода ("text" или "json").
- **async_process** (bool): Флаг асинхронной обработки (True – возвращается job_id).
- **transcriptions** (Optional[Dict[str, Any]]): Дополнительные параметры транскрипции.

**Пример использования:**
```
with open("audio_sample.mp3", "rb") as f:
    audio_data = f.read()

transcription = await client.process_audio(
    audio_file=audio_data,
    provider=Provider.OPENAI,
    format_output="json",
    transcriptions={"task": "transcribe"}
)
print(transcription)
```
------------------------------------------------------------
### 4. Синтез речи – generate_voice

Функция для преобразования текста в речь. Возвращает словарь с результатами (например, аудио в формате base64).

**Параметры:**
- **text** (str): Исходный текст для озвучивания.
- **provider** (Provider): Провайдер синтеза речи.
- **model** (Optional[str]): Название модели (если требуется).

**Пример использования:**
```
voice_data = await client.generate_voice(
    text="Добрый день!",
    provider=Provider.OPENAI
)
print(voice_data)
```
------------------------------------------------------------
### 5. Получение доступных моделей – get_available_models

Позволяет получить список моделей, доступных у провайдера для конкретной функциональности (например, текст, изображение, аудио).

**Параметры:**
- **provider** (Optional[Union[Provider, str]]): Имя провайдера.
- **capability** (Optional[Union[Capability, str]]): Тип функциональности (например, "text", "vision").

**Пример использования:**
```
models = await client.get_available_models(provider=Provider.OPENAI, capability="text")
print("Доступные модели:", models)
```
------------------------------------------------------------
## Модель данных для управления отправкой запроса

Для валидации и корректной упаковки параметров можно использовать Pydantic-модель. Например:
```
from pydantic import BaseModel, Field
from typing import List, Optional, Union

class TextGenerationRequest(BaseModel):
    message: str
    provider: str
    model: Optional[str] = None
    max_tokens: int = Field(default=150, ge=1)
    temperature: float = Field(default=0.7, ge=0, le=1)
    stream: bool = False
    system: Optional[str] = ""
    messages: Optional[List[dict]] = []
    reasoning_effort: Optional[str] = None
    image_bytes: Optional[Union[str, bytes]] = None
```
Такой подход позволит гарантировать корректность типов и упростить дальнейшую отладку и расширение функционала.

------------------------------------------------------------
## Структура проекта

Пример рекомендуемой структуры клиентского проекта:
```
MyClientCLI/
├── cli_client/              # Основной пакет библиотеки
│   ├── __init__.py
│   ├── client.py            # Класс APIClient с реализацией функций generate_text, generate_image, process_audio, generate_voice, get_available_models
│   ├── config.py            # Загрузка конфигураций из переменных окружения и INI-файлов
│   ├── exceptions.py        # Пользовательские исключения (APIClientError, ServerError, AuthenticationError, ProviderNotImplementedError)
│   ├── utils.py             # Вспомогательные классы и перечисления (Provider, Capability)
│   ├── models.py            # Вспомогательные классы 
│   └── __main__.py          # Точка входа для CLI (функция main)
├── tests/                   # Тесты (например, test_client.py)
│   └── test_client.py
├── LICENSE                  # Лицензия проекта
├── README.md                # Данный файл описания
└── pyproject.toml           # Конфигурация сборки и метаданные пакета
```
------------------------------------------------------------
## Дальнейшие возможности расширения функционала

Помимо описанных функций, возможны следующие доработки:

• Реализация асинхронного контекстного менеджера (добавить методы __aenter__ и __aexit__) для удобного использования:
```
async with APIClient(base_url="http://localhost:8000") as client:
    # работа с клиентом
```
• Интеграция расширенного логирования (модуль logging) для отладки запросов и ответов.

• Механизм повторных попыток (retries) с экспоненциальной задержкой для временных сбоев подключения.

• Локальное кэширование результатов вызова get_available_models и других часто запрашиваемых данных.

• Расширение возможностей CLI (добавление новых аргументов, настройка дополнительных эндпоинтов и поддержки websocket‑подключений).

• Автоматизированное тестирование (с использованием pytest и CI/CD сервисов).

------------------------------------------------------------
## Лицензия

Этот проект распространяется под лицензией MIT. Подробности смотрите в файле [LICENSE](LICENSE).

------------------------------------------------------------
## Вывод

**CLI Client для Model Provider API** представляет собой мощное решение для интеграции с сервером генерации контента. Библиотека поддерживает не только базовые функции (текст, изображение, аудио), но и расширенные возможности потоковой обработки и асинхронного взаимодействия. Рекомендуется ознакомиться с примерами использования, протестировать работу на тестовом сервере и при необходимости расширять функционал с учётом требований вашего проекта.

Для любых вопросов или предложений по улучшению, пожалуйста, обращайтесь к разработчику.

------------------------------------------------------------
