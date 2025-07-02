from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def msg():
    return "hello fastapi coders"