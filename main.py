import os
import logging

from fastapi import FastAPI
from routes import users, characters, dialogues, messages

logging.basicConfig(level=logging.DEBUG)

app = FastAPI()
app.include_router(users.router)
app.include_router(characters.router)
app.include_router(dialogues.router)
app.include_router(messages.router)

