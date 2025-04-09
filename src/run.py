from uvicorn import run
from .main import app

def start():
    run(app=app, host="0.0.0.0", port=5000)

def dev():
    run(app="src.main:app", port=5000, reload=True)