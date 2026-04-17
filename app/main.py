from fastapi import FastAPI
from app.api.routes import chat

app = FastAPI(title="AI Knowledge Base")

app.include_router(chat.router, prefix="/api")