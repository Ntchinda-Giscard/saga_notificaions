from fastapi import FastAPI
from .database.session import engine, Base
from .routes import notification_routes

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Bus Booking - Notification Service",
    description="Service for sending notifications",
    version="1.0.0"
)

app.include_router(notification_routes.router)

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "NotificationService"}
