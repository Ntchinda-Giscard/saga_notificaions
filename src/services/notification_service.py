from sqlalchemy.orm import Session
from ..database.models import NotificationLog
from ..schemas.notification_schema import NotificationSend

class NotificationService:
    def __init__(self, db: Session):
        self.db = db

    def send_notification(self, notification_data: NotificationSend):
        # Mock sending email/sms
        print(f"SENDING {notification_data.notification_type} TO User {notification_data.user_id}: {notification_data.message}")
        
        new_log = NotificationLog(
            user_id=notification_data.user_id,
            message=notification_data.message,
            notification_type=notification_data.notification_type,
            status="SENT"
        )
        self.db.add(new_log)
        self.db.commit()
        self.db.refresh(new_log)
        return new_log

    def get_logs(self):
        return self.db.query(NotificationLog).all()
