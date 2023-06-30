import logging
from fastapi import FastAPI
from routes import users, characters, dialogues, messages
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

logging.basicConfig(level=logging.DEBUG)

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

"""
Client-server interaction is done via REST API. Server provides following endpoints:

"""