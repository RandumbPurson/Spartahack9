from flask import Flask, render_template, request
from NextImg import ImageNavigator
from User import User

app = Flask(__name__)

user = User()
nav = ImageNavigator("static/memes", "static/imagetags.json")

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/swipe")
def swipe():
    return render_template("tinder.html")

@app.route("/memes")
def next_meme():
    return nav.find_next_unseen_image()

    # if request.method == "GET":
    # if request.method == "PUT":
    #     user.updatePrefs(request.get_json())
        
