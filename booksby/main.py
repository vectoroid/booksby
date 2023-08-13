"""
main file
"""
import emmett

app = emmett.App(__name__)

@app.route("/")
async def hello():
    return "<html><head><title>Hello from Emmett</title></head><body><h2>Hello, world!</h2></body></html>"