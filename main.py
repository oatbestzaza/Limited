from fastapi import FastAPI
import uvicorn

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