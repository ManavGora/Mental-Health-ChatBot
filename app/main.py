# app/main.py
from fastapi import FastAPI
from app.rag import rag_router
from app.classification import classification_router

app = FastAPI()

app.include_router(rag_router, prefix="/rag")
app.include_router(classification_router, prefix="/classification")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Mental Health Chatbot API"}
