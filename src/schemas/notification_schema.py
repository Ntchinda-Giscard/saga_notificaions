from pydantic import BaseModel
from datetime import datetime

class NotificationSend(BaseModel):
    user_id: int
    message: str
    notification_type: str = "EMAIL"

class NotificationResponse(BaseModel):
    id: int
    user_id: int
    message: str
    status: str
    created_at: datetime
    
    class Config:
        from_attributes = True
