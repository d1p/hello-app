import os
from flask import Flask

app = Flask(__name__)
VERSION = os.getenv("APP_VERSION", "dev")


@app.get("/")
def hello():
    return f"Hello from the homelab! version={VERSION}\n"


@app.get("/healthz")
def healthz():
    return "ok"
