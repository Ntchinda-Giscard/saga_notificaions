from fastapi import FastAPI
from .database.session import init_db
from .routes import notification_routes

app = FastAPI(
    title="Bus Booking - Notification Service",
    description="Service for sending notifications (Email/SMS)",
    version="1.0.0"
)

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(notification_routes.router)

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "NotificationService"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)