import os
import logging
from dotenv import dotenv_values
from fastapi import FastAPI
from routes import users, characters, dialogues, messages
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

logging.basicConfig(level=logging.DEBUG)

# Load environment variables from .env file
env_vars = dotenv_values(".env")

app = FastAPI()
app.include_router(users.router)
app.include_router(characters.router)
app.include_router(dialogues.router)
app.include_router(messages.router)

app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")


# Serve the index.html file as the root path
@app.get("/", response_class=HTMLResponse)
async def get_index():
    return open("frontend/index.html").read()