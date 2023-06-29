import os
import logging

from fastapi import FastAPI
from routes import user

logging.basicConfig(level=logging.DEBUG)

app = FastAPI()
app.include_router(user.router)
