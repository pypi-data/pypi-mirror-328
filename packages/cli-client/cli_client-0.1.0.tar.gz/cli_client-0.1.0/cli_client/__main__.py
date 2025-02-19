# cli_client/__main__.py

import asyncio
import argparse
from cli_client import APIClient, Provider

def main() -> None:
  """
  Точка входа CLI клиента для работы с API-сервером.

  Принимает аргументы:
   --ip: URL сервера (по умолчанию http://localhost:8000).
   --provider: Имя провайдера (например, openai).
   --endpoint: Выбор эндпоинта ("text", "image", "audio", "voice").
   --message: Текстовое сообщение или описание изображения.
  """
  parser = argparse.ArgumentParser(description="CLI клиент для работы с Model Provider API")
  parser.add_argument("--ip", type=str, default="http://localhost:8000", help="Базовый URL сервера")
  parser.add_argument("--provider", type=str, required=True, help="Имя провайдера (например, openai)")
  parser.add_argument("--endpoint", type=str, choices=["text", "image", "audio", "voice"], required=True,
            help="Эндпоинт для вызова")
  parser.add_argument("--message", type=str, help="Сообщение для текстовой генерации или описание изображения")
  
  args = parser.parse_args()
  client = APIClient(base_url=args.ip)
  
  async def run() -> None:
    if args.endpoint == "text":
      result = await client.generate_text(message=args.message or "", provider=Provider(args.provider))
      print("Результат генерации текста:")
      print(result)
    else:
      print(f"Работа с эндпоинтом {args.endpoint} пока не реализована.")
    await client.close()
  
  asyncio.run(run())

if __name__ == "__main__":
  main()
