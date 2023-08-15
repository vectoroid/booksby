"""
main file
"""
from emmett import App

app = App(__name__)

@app.route("/")
async def hello():
    return "Hello, world!"

@app.route("/jsonhello")
async def json_hello():
    return {"message": "Hello, world!"}