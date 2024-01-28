from flask import Flask

app = Flask("chuckl")

@app.route("/")
def hello_world():
    return "<p>Test</p>"
