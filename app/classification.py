# app/classification.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import joblib

classification_router = APIRouter()

# Load the trained classification model
classifier_model = joblib.load("app/models/classifier.pkl")

class DataItem(BaseModel):
    text: str

@classification_router.post("/")
async def classify_endpoint(item: DataItem):
    if not item.text:
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    
    # Predict the category of the text
    prediction = classifier_model.predict([item.text])
    return {"prediction": prediction[0]}
