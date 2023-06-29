import os
import logging

from fastapi import FastAPI
from routes import user
from routes import character
from routes import dialogue

logging.basicConfig(level=logging.DEBUG)

app = FastAPI()
app.include_router(user.router)
app.include_router(character.router)
app.include_router(dialogue.router)

