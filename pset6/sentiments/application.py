from flask import Flask, redirect, render_template, request, url_for

import helpers
from analyzer import Analyzer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "").lstrip("@")
    if not screen_name:
        return redirect(url_for("index"))

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name)
    if not tweets:
        return redirect(url_for("index"))
        
    # absolute paths to lists
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")

    # instantiate analyzer
    analyzer = Analyzer(positives, negatives)

    # TODO
    positive, negative, neutral = 0.0, 0.0, 100.0
    neutral_test = 0.0
    
    # for each tweet:
    for tweet in tweets:
        
        # analyze each tweet
        score = analyzer.analyze_single_tweet(tweet)
        if score > 0.0:
            positive += 1
        elif score < 0.0:
            negative += 1
        else:
            neutral_test += 1
            
    neutral = neutral_test
    
    # keep track of whether each tweet is positive, negative, or neutral

    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)