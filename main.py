from fastapi import FastAPI
import uvicorn
@app.get("/")
async def main():
    return 'Hello World'

@app.get("/test")
async def test():
    return 'Test Tutorial'

@app.get("/add")
async def add(a: int = 0, b: int = 0):
    return a+b

@app.get("/mul")
async def mul(a: int = 0, b: int = 0):
    return a*b

@app.get("/pow")
async def pow(a: int = 0, b: int = 0):
    return math.pow(a,b)
if __name__ == '__main__':
   uvicorn.run(app, host="0.0.0.0", port=80, debug=True) 