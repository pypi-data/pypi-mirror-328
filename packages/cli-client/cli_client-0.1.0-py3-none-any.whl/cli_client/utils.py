from enum import Enum

class Provider(str, Enum):
  """
  Перечисление доступных провайдеров.
  """
  OLLAMA = "ollama"
  GEMINI = "gemini"
  ANTHROPIC = "anthropic"
  OPENAI = "openai"


class Capability(str, Enum):
  """
  Перечисление возможностей провайдеров.
  """
  TEXT = "text"
  VISION = "vision"
  TRANSCRIPTION = "transcription"
  IMAGE = "image"
  VOICE = "voice"