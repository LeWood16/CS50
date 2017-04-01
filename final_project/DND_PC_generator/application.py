from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import gettempdir
from datetime import datetime
import time 

from helpers import *

# configure application
app = Flask(__name__)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response


# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = gettempdir()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

@app.route("/")
@login_required
def index():
    
    # grab user table via user id
    user_table = "user" + str(session["user_id"])
    
    user_table_dict = db.execute("SELECT * FROM :table", table=user_table)
    
    # this value is for iterating through user's table values
    l = len(user_table_dict)
    l = int(l)

    # lookup user cash amount
    cash = db.execute("SELECT cash FROM users WHERE id=:userid", userid=session["user_id"])
    cash = (cash[0]["cash"])
    cash_usd = usd(cash)
    
    # create an object dynamically to flash current share values to template
    current_values = [lookup(user_table_dict[i]["symbol"]) for i in range(0, int(l))]
        # current_values.append(lookup(user_table_dict[i]["symbol"]))
    current_prices = []
    current_prices_usd = []
    total_prices = []
    total_prices_usd = []
    total_account_value = 0

    # create current prices list
    for i in range(0, l):
        current_prices.append(current_values[i]["price"])
        
    # create current prices list in usd form
    for j in range(0, l):
        current_prices_usd.append(usd(current_values[j]["price"]))
       
    # create total prices list (i.e. current price * quantity for each stock) 
    for k in range(0, l):
        total_prices.append(current_prices[k] * user_table_dict[k]["quantity"] ) 
        
        
    # calculate total account value    
    for n in range(0, l):
        total_account_value = total_account_value + total_prices[n]
    total_account_value = total_account_value + cash

    # create total prices list in usd form
    for m in range(0, l):
        total_prices_usd.append(usd(total_prices[m]))
    

    return render_template("index.html", user_table_dict=user_table_dict, l=l, current_prices=current_prices, cash=cash, cash_usd=cash_usd, current_prices_usd=current_prices_usd, total_prices_usd=total_prices_usd, total_account_value=usd(total_account_value))

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""

    # forget any user_id
    session.clear()

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            flash("must provide username")
            return redirect(url_for("login"))

        # ensure password was submitted
        elif not request.form.get("password"):
            flash("must provide password")
            return redirect(url_for("login"))            

        # query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))

        # ensure username exists and password is correct
        if len(rows) != 1 or not pwd_context.verify(request.form.get("password"), rows[0]["hash"]):
            flash("invalid username and/or password")
            return redirect(url_for("login"))            

        # remember which user has logged in
        session["user_id"] = rows[0]["id"]
        
        # create table of user purchases on register instance;
        # table name is "user" concatenated with user_id integer;
        # if table for user does not exist, create it!
        table_name = "user" + str(session["user_id"])
        count = db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=:table_name", table_name=table_name)
        if len(count) == 0:
            db.execute("CREATE TABLE :table_name (id INTEGER PRIMARY KEY, symbol TEXT NOT NULL, name TEXT NOT NULL, quantity INTEGER NOT NULL)", table_name=table_name)
     
        # redirect user to home page
        flash("you were successfully logged in")
        return redirect(url_for("index"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    
    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

    # require that user put in a username
        
        # render apology if blank
        if not request.form.get("username"):
            flash("must provide username")
            return redirect(url_for("register"))

        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))

        # render apology if username already exists
        if len(rows) == 1:
            flash("username already exists")
            return redirect(url_for("register"))

    # require that user put in a password
        
        # ensure password was submitted
        elif not request.form.get("password"):
            flash("must provide password")
            return redirect(url_for("register"))

        # ensure password confirmation was attempted
        elif not request.form.get("confirm"):
            flash("must confirm password")
            return redirect(url_for("register"))

        # ensure password confirmation was successful
        elif request.form.get("confirm") != request.form.get("password"):
            flash("passwords do not match")
            return redirect(url_for("register"))

        else:
            
            # TODO
            """
            # create variables to pass into user's table row
            username = request.form.get("username")
            hash = pwd_context.encrypt(request.form.get("password"))
            cash = 10000

            # create user account, via a table row
            db.execute("INSERT INTO users (username, hash, cash) VALUES (:username, :hash, :cash)", username=username, hash=hash, cash=cash)


            # log the user in, and redirect them to the homepage
            login()
            return redirect(url_for("index"))
            """
    """Register user."""
    return render_template("register.html")
