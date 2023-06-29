import os
import logging

from fastapi import FastAPI
from routes import users
from routes import characters
from routes import dialogues

logging.basicConfig(level=logging.DEBUG)

app = FastAPI()
app.include_router(user.router)
app.include_router(character.router)
app.include_router(dialogue.router)

