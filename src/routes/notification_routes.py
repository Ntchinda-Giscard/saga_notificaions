from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database.session import get_db
from ..services.notification_service import NotificationService
from ..schemas.notification_schema import NotificationSend, NotificationResponse

router = APIRouter(
    prefix="/notifications",
    tags=["notifications"]
)

def get_service(db: Session = Depends(get_db)) -> NotificationService:
    return NotificationService(db)

@router.post("/send", response_model=NotificationResponse)
def send_notification(
    notification_data: NotificationSend,
    service: NotificationService = Depends(get_service)
):
    return service.send_notification(notification_data)

@router.get("/logs", response_model=List[NotificationResponse])
def get_logs(service: NotificationService = Depends(get_service)):
    return service.get_logs()
