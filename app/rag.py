# app/rag.py
from fastapi import APIRouter, HTTPException
from transformers import pipeline

rag_router = APIRouter()

# Load the pre-trained LLM model
llm_model = pipeline("text-generation", model="gpt2")  # Use "gpt2" or another suitable model

@rag_router.post("/")
async def rag_endpoint(prompt: str):
    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt cannot be empty")
    
    # Generate relevant articles based on the prompt
    response = llm_model(prompt, max_length=150)
    return {"response": response}
