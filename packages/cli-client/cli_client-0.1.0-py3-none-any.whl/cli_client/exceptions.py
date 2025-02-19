class APIClientError(Exception):
  """Базовое исключение для APIClient."""
  pass


class ServerError(APIClientError):
  """Исключение для ошибок на стороне сервера."""
  pass


class AuthenticationError(APIClientError):
  """Исключение для ошибок аутентификации."""
  pass


class ProviderNotImplementedError(APIClientError):
  """Исключение, если выбранный провайдер не реализован."""
  pass
