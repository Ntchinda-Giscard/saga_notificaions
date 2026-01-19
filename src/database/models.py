from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .session import Base

class NotificationLog(Base):
    __tablename__ = "notification_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True, nullable=False)
    message = Column(String, nullable=False)
    notification_type = Column(String, nullable=False) # EMAIL, SMS
    status = Column(String, default="SENT")
    created_at = Column(DateTime, default=datetime.utcnow)
