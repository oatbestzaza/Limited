from fastapi import FastAPI
import uvicorn
from fastapi.responses import PlainTextResponse
import fasttext 
import fasttext.util

@app.get("/model")
async def modeloutput(a):
    a = a + 2
    return a
    
