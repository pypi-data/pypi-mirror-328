# examples/integration_example.py

import asyncio
import json
import pytest
from cli_client.client import APIClient
from cli_client.utils import Provider, Capability

base_url = "http://185.180.230.207:8001"
client = APIClient(base_url=base_url, auth=("developer", "developer"))

@pytest.mark.asyncio
async def test_get_all_models():
  # Замените base_url на адрес вашего тестового сервера
  results = {}

  try:
    i = 0
    # Перебираем все комбинации провайдеров и возможностей
    for provider in Provider:
      for capability in Capability:
        print(f"Запрос моделей для провайдера: {provider.value}, возможности: {capability.value}")
        response = await client.get_available_models(provider=provider, capability=capability)
        results[f"{provider.value}_{capability.value}"] = response
        
    # Выводим полный словарь ответов
    print("Полный список моделей, полученный с сервера:")
    print(json.dumps(results, indent=2, ensure_ascii=False))
    
    # Пример простой проверки: каждая пара должна вернуть словарь (в зависимости от логики сервера можно делать более сложные проверки)
    for key, data in results.items():
      assert isinstance(data, list), f"Для {key} ожидался dict, получено: {type(data)}"
  finally:
    await client.close()


@pytest.mark.asyncio
async def test_generate_text_for_all_providers(stream_modes):
  # Укажите базовый URL тестового сервера
  try:
    for provider in Provider:
      message_text = f"Привет от {provider.value}. Напиши 2 абзаца с разметками markdown."
      # Для каждого провайдера запрашиваем список моделей для текстовой генерации
      models = await client.get_available_models(provider=provider, capability=Capability.TEXT)
      
      # Проверяем, что результат имеет тип list (или, если у вас ожидается dict – отредактируйте проверку)
      assert isinstance(models, list), (
        f"Для провайдера {provider.value} ожидался список моделей, получен: {type(models)}"
      )
      
      # Если у провайдера нет доступных моделей – можно пропустить этот кейс
      if not models:
        pytest.skip(f"Нет доступных моделей для провайдера {provider.value}")
        
      # Предполагаем, что первая модель задаётся в виде строки (если формат другой, извлеките необходимое поле)
      first_model = models[0] if isinstance(models[0], str) else models[0].get("name")
      assert first_model, f"Не удалось определить первую модель для провайдера {provider.value}"
      
      for stream in stream_modes:
        print(f"СТАРТ {provider.value}: {first_model} | STREAM {stream}")
        # Формируем простое текстовое сообщение
        
        # 1. Вызов без потока (stream=False)
        result = await client.generate_text(
          message=message_text,
          max_tokens = 500,
          provider=provider,
          model=first_model,
          stream=stream
        )
        if stream == True:
          streamed_text = ""
          async for chunk in result:
            streamed_text += chunk
        else: streamed_text = result
        print(f"STREAM {stream} result for {provider.value}: {streamed_text}")
        assert isinstance(streamed_text, str), (
          f"Ожидалась строка в не потоковом режиме для провайдера {provider.value}"
        )
  finally:
    await client.close()
    
@pytest.mark.asyncio
async def test_visual_for_all_providers(stream_modes):
  # Укажите путь к тестовому изображению
  image_path = "tests/scheme.png"
  # Читаем изображение
  with open(image_path, "rb") as img:
    image_data = img.read()
  # Список режимов стриминга
  
  try:
    for provider in Provider:
      message_text = f"Привет от {provider.value}. Дай подробное описание изображению."
      # Получаем список моделей для визуальной интерпретации
      models = await client.get_available_models(provider=provider, capability=Capability.VISION)
      # Если моделей нет – пропускаем
      if not models:
        pytest.skip(f"Нет доступных моделей для {provider.value} с возможностью VISION")
      # Определяем первую модель: если запись — строка или словарь с ключом "name"
      first_model = models[0] if isinstance(models[0], str) else models[0].get("name")
      assert first_model, f"Не удалось определить первую модель для {provider.value}"
      
      for stream in stream_modes:
        print(f"СТАРТ {provider.value}: {first_model} | Изображение: {image_path} | STREAM {stream}")
        # Формируем payload; передаём стрим-флаг
        result = await client.generate_text(
          message=message_text,
          image_bytes=image_data,
          max_tokens = 500,
          provider=provider,
          model=first_model,
          stream=stream
        )
        
        if stream == True:
          streamed_text = ""
          async for chunk in result:
            streamed_text += chunk
        else: streamed_text = result
        print(f"STREAM {stream} result for {provider.value}: {streamed_text}")
        assert isinstance(streamed_text, str), (
          f"Ожидалась строка в не потоковом режиме для провайдера {provider.value}"
        )
  finally:
    await client.close()
    
@pytest.mark.asyncio
async def test_generate_image_openai_success():
    """
    Тест успешной генерации изображения через OpenAI.
    """
    try:
      prompt = "A cute cat wearing a hat"
      result = await client.generate_image(prompt=prompt, provider=Provider.OPENAI)
      # Базовая проверка: ожидаем словарь с каким-то результатом
      assert isinstance(result, dict), "Ожидался словарь с результатом"
      # Дополнительные проверки (зависят от формата ответа):
      assert "image_url" in result or "used_size" in result, "Ожидался 'image_url' или 'used_size' в ответе" #URL будет если это будет DALL-E 3, data - если более старые.
      if "image_url" in result:
          assert isinstance(result["image_url"], str)
          assert result["image_url"].startswith("http")
      elif "data" in result:
          assert isinstance(result["used_size"], str)
            
    finally:
        await client.close()

@pytest.mark.asyncio
async def test_generate_image_invalid_provider():
    """
    Тест с некорректным провайдером.
    """
    client = APIClient(base_url=base_url, auth=("developer", "developer"))
    try:
        prompt = "Anything"
        with pytest.raises(Exception) as exc_info: #aiohttp.ClientResponseError
            await client.generate_image(prompt=prompt, provider=Provider.GEMINI)  # Используем Gemini
        # Проверяем, что возникло исключение, и сообщение об ошибке содержит нужный текст
        assert "Неверный провайдер" in str(exc_info.value) or "Not Found" in str(exc_info.value)
    finally:
        await client.close()
       
async def test_transcription_for_all_providers():
    """
    Тестирует транскрибацию аудио для всех доступных провайдеров.
    """
    audio_path = "tests/generated_voice_1317.opus"  # Путь к тестовому аудиофайлу

    # Читаем ожидаемую транскрипцию из файла
    with open("tests/transcribe.txt", "r", encoding="utf-8") as f:
        expected_transcription = f.read().strip()

    # Читаем аудиофайл в бинарном виде
    with open(audio_path, "rb") as audio_file:
        audio_data = audio_file.read()

    try:
        for provider in Provider:
            if provider.value in ["gemini", "anthropic"]:
              continue
            # Получаем список моделей для транскрипции
            models = await client.get_available_models(provider=provider, capability=Capability.TRANSCRIPTION)

            # Если моделей нет – пропускаем
            if not models:
                pytest.skip(f"Нет доступных моделей для {provider.value} с возможностью TRANSCRIPTION")

            # Определяем первую модель (аналогично другим тестам)
            first_model = models[0] if isinstance(models[0], str) else models[0].get("name")
            assert first_model, f"Не удалось определить первую модель для {provider.value}"

            print(f"СТАРТ {provider.value}: {first_model} | Аудио: {audio_path}")

            # Вызываем транскрибацию (stream=False, для простоты)
            result = await client.process_audio(
                audio_file=audio_data,
                provider=provider,
                format_output="text", #  Указываем желаемый формат "text"
                transcriptions={"task":"transcribe"}
            )
            # format output можно не указывать, значение по умолчанию text

            print(f"Результат транскрипции для {provider.value}: {result}")
            
            # Сравниваем полученный результат с ожидаемым
            assert result.strip() == expected_transcription, (
                f"Транскрипция для {provider.value} не совпадает с ожидаемой.\n"
                f"Получено: {result.strip()}\n"
                f"Ожидалось: {expected_transcription}"
            )

    finally:
        await client.close() 
# Для запуска теста без pytest можно использовать следующий блок:
if __name__ == "__main__":
  #asyncio.run(test_get_all_models())
  #asyncio.run(test_generate_text_for_all_providers([True]))
  #asyncio.run(test_visual_for_all_providers([True]))
  #asyncio.run(test_generate_image_openai_success())
  ##asyncio.run(test_generate_image_invalid_provider())
  asyncio.run(test_transcription_for_all_providers())
  
  
  
  
  pass