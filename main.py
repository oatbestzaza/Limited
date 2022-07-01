from fastapi import FastAPI
import uvicorn
from fastapi.responses import PlainTextResponse
import fasttext 
import fasttext.util

@app.get("/model")
async def modeloutput(txt):
    model = fasttext.load_model('r_model_50dgamestatus.bin')
    return {model.predict(txt, k=5, threshold=0.01)}
    
