#Author: Chatchawal Sangkeettrakarn
#Date: September 20,2020.

from fastapi import FastAPI
import uvicorn
# import numpy as np
# import re
# import math
# import requests
# from bs4 import BeautifulSoup
from fastapi.responses import PlainTextResponse

app = FastAPI()

def result(res):
    return {"result":res}

@app.get("/")
async def main():
    return 'Hello World'

@app.get("/ngrams")
def bigrams(text):
    #text = 'chatchawal 1234'
    num = 2
    #print(len(text))
    sto = []
    #def ngrams(text,num):
    for x in range(len(text)-(num-1)):
        print(x,text[x:x+num])
        sto.append(text[x:x+num])
    #ngrams(text,num)
    return sto