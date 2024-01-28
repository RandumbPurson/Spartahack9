from os import environ as env
from flask import Flask, render_template, request, session, url_for, redirect
from urllib.parse import quote_plus, urlencode
from authlib.integrations.flask_client import OAuth
from NextImg import ImageNavigator
from User import User
from DB import DB
from dotenv import find_dotenv, load_dotenv

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

app = Flask(__name__)

db = DB("database")
user = User(db.db)
nav = ImageNavigator("static/memes", "static/imagetags.json", db.db)

oauth = OAuth(app)

oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration'
)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/swipe")
def swipe():
    return render_template("tinder.html")

@app.route("/memes", methods=["GET", "PUT"])
def next_meme():
    if request.method == "GET":
        return nav.find_next_unseen_image()
    if request.method == "PUT":
        return user.updatePrefs(request.get_json())

@app.route("/login")
def login():
    return render_template("login.html")
    # return oauth.auth0.authorize_redirect(
    #     redirect_uri=url_for("callback", _external=True)
    # )

@app.route("/auth")
def auth():
    user.login(request.args["username"])
    return redirect("/swipe")

# @app.route("/callback", methods=["GET", "POST"])
# def callback():
#     token = oauth.auth0.authorize_access_token()
#     session["user"] = token
#     return redirect("/")
#
# @app.route("/logout")
# def logout():
#     session.clear()
#     return redirect(
#         "https://" + env.get("AUTH0_DOMAIN")
#         + "/v2/logout?"
#         + urlencode(
#             {
#                 "returnTo": url_for("home", _external=True),
#                 "client_id": env.get("AUTH0_CLIENT_ID"),
#             },
#             quote_via=quote_plus,
#         )
#     )
