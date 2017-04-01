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

# custom filter
app.jinja_env.filters["usd"] = usd

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
    cash = cash[0]["cash"]
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

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        
        # require that a user input a stock symbol
        if request.form.get("symbol") == "" or lookup(request.form.get("symbol")) is None:
            flash("must provide a stock symbol")
            return redirect(url_for("buy"))

        # require that user input a positive integer for a stock quantity
        elif request.form.get("quantity") == "" or int(request.form.get("quantity")) < 1:
            flash("must provide a positive integer")
            return redirect(url_for("buy"))

        else:
            # store user-provided symbol in variable
            s = request.form.get("symbol")
       
            # store a dict of that symbol's lookup values
            symbol_dict = lookup(s)
            # returns {name:name, price:price, symbol:symbol}
            
            
            # if user has insufficient funds, flash message
            cash = db.execute("SELECT cash FROM users WHERE id = :user_id", user_id=session["user_id"])
            cash = cash[0]["cash"]
            cash = int(cash)
            
            if (int(symbol_dict["price"]) * int(request.form.get("quantity"))) > cash:
                flash("insufficient funds")
                return redirect(url_for("buy"))

            else:
                
                # grab user table via user id
                user_table = "user" + str(session["user_id"])
                
                # create values for row insertion
                symbol = symbol_dict["symbol"]
                name = symbol_dict["name"]
                quantity = request.form.get("quantity")
                price = symbol_dict["price"]
                
                stock_already_owned = db.execute("SELECT symbol FROM :user_table WHERE symbol=:symbol", user_table=user_table, symbol=symbol)

                # if user has stock of this type, update that row on user table
                if stock_already_owned:
                    
                    # update that row in user's table
                    current_quantity = db.execute("SELECT quantity FROM :user_table WHERE symbol=:symbol", user_table=user_table, symbol=symbol)
                    current_quantity = current_quantity[0]["current_quantity"]
                    quantity = int(quantity) + int(current_quantity)
                    db.execute("UPDATE :user_table SET quantity=:quantity WHERE symbol=:symbol", user_table=user_table, quantity=quantity, symbol=symbol)
                    
                else:

                    # else, create a new row on user table
                    db.execute("INSERT INTO :user_table (symbol, name, quantity) VALUES (:symbol, :name, :quantity)", user_table=user_table, symbol=symbol, name=name, quantity=quantity)
            
                # figure out how much cash to take out of user's account
                stockPurchase = price * int(quantity)
                cash = cash - stockPurchase
            
                # update user's cash amount
                db.execute("UPDATE users SET cash = :cash WHERE id = :user_id", cash=cash, user_id=session["user_id"])
                 
                # update purchase_history table
                user_name = db.execute("SELECT username FROM users WHERE id=:id", id=session["user_id"])
                user_name = user_name[0]["user_name"]
                time_and_date = str(datetime.fromtimestamp(time.time()))

                # override quantity for purchase_history table
                quantity = request.form.get("quantity")
                quantity = int(quantity)
                
                db.execute("INSERT INTO purchase_history (username, symbol, name, quantity, price, time_and_date, type) VALUES (:username, :symbol, :name, :quantity, :price, :time_and_date, :type)", username=user_name, symbol=symbol, name=name, quantity=quantity, price=price, time_and_date=time_and_date, type="Buy")

                return render_template("buy.html", cash=usd(cash))
                
    else:
        
        # show user how much cash is in their account
        cash = db.execute("SELECT cash FROM users WHERE id = :user_id", user_id=session["user_id"])
        cash = cash[0]["cash"]
        cash = usd(cash)
        return render_template("buy.html", cash=cash)

    
@app.route("/history")
@login_required
def history():
    """Show history of transactions."""
    
    # grab all of the rows from the purchase_history table that belong to the current user
    username = db.execute("SELECT username FROM users WHERE id=:userid", userid=session["user_id"])
    username = username[0]["username"]
    history = db.execute("SELECT * FROM purchase_history WHERE username=:username", username=username)

    # grab length of purchase_history table to use to generate table
    l = len(history)

    return render_template("history.html", history=history, l=l)

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
        session["user_id"] = rows[0]["user_id"]
        
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

@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":
        
        # require that a user input a stock symbol
        if request.form.get("symbol") == "" or lookup(request.form.get("symbol")) is None:
            flash("must provide a stock symbol")
            return redirect(url_for("quote"))

        else:
            # store user-provided symbol in variable
            s = request.form.get("symbol")
       
            # store a dict of that symbol's lookup values
            symbol_dict = lookup(s)
            # returns {name:name, price:price, symbol:symbol}
    
            return render_template("quoted.html", name=symbol_dict["name"], price=usd(symbol_dict["price"]), symbol=symbol_dict["symbol"])
    else:
    
        return render_template("quote.html")
     
   


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
            
            # create variables to pass into user's table row
            username = request.form.get("username")
            hash = pwd_context.encrypt(request.form.get("password"))
            cash = 10000

            # create user account, via a table row
            db.execute("INSERT INTO users (username, hash, cash) VALUES (:username, :hash, :cash)", username=username, hash=hash, cash=cash)


            # log the user in, and redirect them to the homepage
            login()
            return redirect(url_for("index"))
            
    """Register user."""
    return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock."""
    cash = db.execute("SELECT cash FROM users WHERE id = :user_id", user_id=session["user_id"])
    cash = cash[0]["cash"]

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        
        if request.form.get("symbol") == "":
            flash("must provide a stock symbol")
            return redirect(url_for("sell"))
            
        elif request.form.get("quantity") == "":
            flash("must provide a stock quantity")
            return redirect(url_for("sell"))
        else:
            # store quantity of stocks
            sell_quantity = request.form.get("quantity")
            sell_quantity = int(sell_quantity)

            # store current price of stocks
            p = request.form.get("symbol")
            p = lookup(p)
            
            # store name of stock for table update
            name = p["name"]
            p = p["price"]
            
            # grab user table via user id
            user_table = "user" + str(session["user_id"])
            
            
            # grab current quantity of this stock from user table
            symbol = request.form.get("symbol")
            symbol = symbol.upper()
            
            current_quantity = db.execute("SELECT quantity from :user_table WHERE symbol=:symbol", user_table=user_table, symbol=symbol)
            

            # set an exception check in case user has no shares of that type 
            try:
                current_quantity = current_quantity[0]["current_quantity"]
            except IndexError:
                current_quantity = 0


            # create variable to update user's cash value after stock sale
            new_cash_value = sell_quantity * p
            new_cash_value = cash + new_cash_value
            
            # if stock's quantity would decrease to less than zero:
                # raise apology, "you don't own that many shares"
            if (current_quantity - sell_quantity < 0):
                flash("you don't own that many shares")
                return redirect(url_for("sell"))

            # else if stock's quantity would decrease to zero:
            elif (current_quantity - sell_quantity == 0):
                
                # close that particular row in user's table
                db.execute("DELETE from :table WHERE symbol=:symbol", table=user_table, symbol=symbol)
                
                # update cash value with new cash value in user table
                db.execute("UPDATE users SET cash = :cash WHERE id=:user_id", cash=new_cash_value, user_id=session["user_id"])
                
                # update purchase_history table
                user_name = db.execute("SELECT username FROM users WHERE id=:id", id=session["user_id"])
                user_name = user_name[0]["user_name"]
                time_and_date = datetime.fromtimestamp(time.time())
                time_and_date = str(time_and_date)
                
                # fix quantity bug that overrode current quantity with sold quantity
                current_quantity = current_quantity - sell_quantity
                
                db.execute("INSERT INTO purchase_history (username, symbol, name, quantity, price, time_and_date, type) VALUES (:username, :symbol, :name, :quantity, :price, :time_and_date, :type)", username=user_name, symbol=symbol, name=name, quantity=sell_quantity, price=p, time_and_date=time_and_date, type="Sell")

                return render_template("sell.html", cash=usd(new_cash_value))
            # else, sell the stocks;
            else:
                
                # fix quantity bug that overrode current quantity with sold quantity
                current_quantity = current_quantity - sell_quantity

                
                # update cash value with new cash value
                db.execute("UPDATE users SET cash = :cash WHERE id = :user_id", cash=new_cash_value, user_id=session["user_id"])

                # update row for particular stock value
                db.execute("UPDATE :table SET quantity = :quantity WHERE symbol=:symbol", table=user_table, quantity=current_quantity, symbol=symbol)
                
                # update purchase_history table
                user_name = db.execute("SELECT username FROM users WHERE id=:id", id=session["user_id"])
                user_name = user_name[0]["user_name"]
                time_and_date = datetime.fromtimestamp(time.time())
                time_and_date = str(time_and_date)
                
                # override quantity for purchase_history table
                quantity = request.form.get("quantity")
                quantity = int(quantity)
                
                db.execute("INSERT INTO purchase_history (username, symbol, name, quantity, price, time_and_date, type) VALUES (:username, :symbol, :name, :quantity, :price, :time_and_date, :type)", username=user_name, symbol=symbol, name=name, quantity=sell_quantity, price=p, time_and_date=time_and_date, type="S")


                return render_template("sell.html", cash=usd(new_cash_value))
            
    else:
    
        return render_template("sell.html", cash=usd(cash))
        
@app.route("/options", methods=["GET", "POST"])
@login_required
def options():
    
    """Store additional features for the user."""
    
    if request.method == "GET":
        return render_template("options.html")
        
    # else if post method:
    else:
        # if adding cash is what the user wants to do:
        if request.form["btn"] == "cash":
            dollars=request.form.get("dollars")
            cents=request.form.get("cents")
            
            # if both were left blank, render apology;
            if dollars == "" and cents == "":
                flash("you must enter a value")
                return redirect(url_for("options"))

            # if one is blank and the other is not a digit, render apology;
            elif dollars == "" and not cents.isdigit():
                flash("must enter positive integers")
                return redirect(url_for("options"))              
            elif not dollars.isdigit() and cents == "":
                flash("must enter positive integers")
                return redirect(url_for("options")) 
                
            # if neither is a digit, render apology;
            elif not dollars.isdigit() and not cents.isdigit():
                flash("must enter positive integers")
                return redirect(url_for("options")) 
                
            # if one is blank and the other is a digit, convert them to integers;
            elif dollars == "" and cents.isdigit():
                dollars = 0
                cents = int(cents)
            elif dollars.isdigit() and cents == "":
                dollars = int(dollars)
                cents = 0

            # if both are digits, convert them to integers;
            else:
                dollars = int(dollars)
                cents = int(cents)
                
                
            # if cents digit is too high or too low, return apology
            if (cents < 0) or (cents > 99):
                flash("cents must be between 0 and 99")
                return redirect(url_for("options")) 

            # if cents value is between 1 and 9, convert it to an appropriate float
            elif cents > 0 and cents < 10:
                cents = "0.0" + str(cents)
                cents = float(cents)

            # finish converting cent to float if it is between 10 and 99;
            # combine the dollar amount to a single float value;
            else:
                cents = "0." + str(cents)
                cents = float(cents)

            
            # add cash to user's account; show user how much cash was added on completion
            cash_to_add = dollars+cents    
            
            current_cash = db.execute("SELECT cash FROM users where id=:userid", userid=session["user_id"])
            current_cash = current_cash[0]["current_cash"]
            current_cash = cash_to_add + current_cash
            db.execute("UPDATE users SET cash=:current_cash WHERE id=:userid", current_cash=current_cash, userid=session["user_id"])
            
            flash("Cash has been added to your account. Your new balance is " + str(usd(current_cash)) + ".")
            return render_template("options.html")



        # else if changing the password is what the user wants to do:
        elif request.form["btn"] == "pass":
            
            # query database for username (reinstantiate for this module)
            username = db.execute("SELECT * FROM users WHERE id=:userid", userid=session["user_id"])
            username = username[0]["username"]
            rows = db.execute("SELECT * FROM users WHERE username=:user", user=username)

            # if old does not match user's pass, flash("old password is incorrect")
            if not pwd_context.verify(request.form.get("old"), rows[0]["hash"]):
                flash("old password is incorrect")
                return redirect(url_for("options"))
                
            # elif new is blank, flash("passwords do not match")
            elif request.form.get("new") == "":
                flash("passwords do not match")
                return redirect(url_for("options"))
            
            
            # elif confirm is blank, flash("passwords do not match")
            elif request.form.get("confirm") == "":
                flash("passwords do not match")
                return redirect(url_for("options"))
               
            # elif new != confirm, flash("passwords do not match")
            elif request.form.get("new") != request.form.get("confirm"):
                flash("passwords do not match")
                return redirect(url_for("options"))           
            
            # else, update the password!
            else:
                hash = pwd_context.encrypt(request.form.get("confirm"))
                db.execute("UPDATE users SET hash=:hash WHERE id=:id", hash=hash, id=session["user_id"])
                flash("password has been successfully changed")
                return redirect(url_for("options"))           