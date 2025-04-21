from pydantic import BaseModel
from methodos.models.config import Environment

class CheckinResponse(BaseModel):
  checkin_id: str
  reporting_url: str
  metrics_url: str
  status_url: str
  version: str
  environment: Environment

  
