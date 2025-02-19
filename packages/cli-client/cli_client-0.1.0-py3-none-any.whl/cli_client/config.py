import os
import configparser
from typing import Optional, Dict, Any

DEFAULT_CONFIG: Dict[str, Any] = {
  "base_url": "http://localhost:8000",
  "auth": None,
}


def load_from_env() -> Dict[str, Any]:
  """
  Загружает конфигурацию из переменных окружения.

  Переменные:
    MPM_BASE_URL – базовый URL сервера.
    MPM_AUTH_USER и MPM_AUTH_PASS – креды для аутентификации.

  Returns:
    Dict[str, Any]: Словарь конфигураций.
  """
  config = {}
  base_url = os.environ.get("MPM_BASE_URL")
  if base_url:
    config["base_url"] = base_url
  auth_user = os.environ.get("MPM_AUTH_USER")
  auth_pass = os.environ.get("MPM_AUTH_PASS")
  if auth_user and auth_pass:
    config["auth"] = (auth_user, auth_pass)
  return config


def load_from_file(filepath: str) -> Dict[str, Any]:
  """
  Загружает конфигурацию из INI-файла.

  Args:
    filepath (str): Путь к конфигурационному файлу.

  Returns:
    Dict[str, Any]: Словарь конфигураций.
  """
  parser = configparser.ConfigParser()
  parser.read(filepath)
  config = {}
  if "server" in parser:
    config["base_url"] = parser["server"].get("base_url", DEFAULT_CONFIG["base_url"])
    user = parser["server"].get("auth_user", None)
    password = parser["server"].get("auth_pass", None)
    if user and password:
      config["auth"] = (user, password)
  return config

def load_config(config_path: Optional[str] = None) -> Dict[str, Any]:
  """
  Объединяет конфигурации по умолчанию, из переменных окружения и из файла.

  Args:
    config_path (Optional[str]): Путь к файлу конфигурации.

  Returns:
    Dict[str, Any]: Итоговый словарь конфигураций.
  """
  config = DEFAULT_CONFIG.copy()
  config.update(load_from_env())
  if config_path:
    config.update(load_from_file(config_path))
  return config