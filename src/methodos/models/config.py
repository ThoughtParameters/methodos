import enum
import operator
from pydantic import BaseModel
from pathlib import Path

class LogLevel(str, enum.Enum):
  DEBUG = "DEBUG"
  INFO = "INFO"
  WARNING = "WARNING"
  ERROR = "ERROR"
  CRITICAL = "CRITICAL"

class FactsProvider(str, enum.Enum):
  FACTER = "FACTER"
  OHAI = "OHAI"
  METHODOS = "METHODOS"
  CUSTOM = "CUSTOM"

class Environment(str, enum.Enum):
  PRODUCTION = "PRODUCTION"
  DEVELOPMENT = "DEVELOPMENT"
  STAGING = "STAGING"
  LOCAL = "LOCAL"
  TEST = "TEST"
  QA = "QA"
  UAT = "UAT"
  NONE = "NONE"

class Config(BaseModel):
  operator_url: str = "https://operator.votra.io/"
  ssl_verify: bool = True
  access_key: str
  secret_key: str
  log_level: LogLevel = LogLevel.INFO
  facts_provider: FactsProvider = FactsProvider.METHODOS


