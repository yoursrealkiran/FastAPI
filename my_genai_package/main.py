from fastapi import FastAPI
from my_genai_package.config import settings
from my_genai_package.routers import chat

app = FastAPI(title=settings.app_name, version="1.0.0")

app.include_router(chat.router)