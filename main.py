import os
import logging

from fastapi import FastAPI
from routes import user
from routes import character

logging.basicConfig(level=logging.DEBUG)

app = FastAPI()
app.include_router(user.router)
app.include_router(character.router)
