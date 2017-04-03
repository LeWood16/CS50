from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import gettempdir
import markdown
from flask import Markup



app = Flask(__name__)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        return render_template("game.html")
        
        
        
@app.route('/game.html', methods=["GET", "POST"])
def game():
    if request.method == "GET":
        return render_template("game.html")
    else:
        # look into adding markdown, so you can render questions as they 
        # would appear on a stackoverflow post, or a blog about programming
        return render_template("game.html")


    
