from flask import Flask, render_template, request
from NextImg import ImageNavigator
from User import User

app = Flask(__name__)

user = User()

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/memes", methods=["GET", "PUT"])
def next_meme():
    print(request)
    if request.method == "GET":
        return nav.find_next_unseen_image()
    if request.method == "PUT":
        user.updatePrefs(request.get_json())
        
