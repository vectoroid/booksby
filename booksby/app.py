"""
main file
"""
from emmett import App

app = App(__name__)

@app.route("/")
async def hello():
    return "<html><head><title>Hello from Emmett</title></head><body><h2>Hello, world!</h2></body></html>"