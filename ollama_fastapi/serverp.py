from fastapi import FastAPI
from ollama import Client

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello world", "good to see you"}


@app.get("/contact")
def contactpage():
    return {"email": "azazshaikh2703@gmail.com"}
__import__('pprint').pprint(expression)
🌓
