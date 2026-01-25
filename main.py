# from fastapi import FastAPI

# app = FastAPI() # FastAPI class is initialized into an object (app), we will create endpoints by using app as a decorater

# @app.get("/") # app used as decorater
# def read_root():
#     return {"message": "This is my first API"}

# @app.get("/name") # app used as decorater
# def read_root():
#     return {"message": "Hi Kiran"}



from fastapi import FastAPI
from config import settings

app = FastAPI()

@app.get("/info")
def get_info():
    return {
        "debug": settings.debug,
        "database_url": settings.database_url,
    }