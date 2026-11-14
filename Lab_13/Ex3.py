# Create a simple Flask application to retrieve memes 
# Kaili Takara
# November 13th, 2026

import requests
from flask import Flask, render_template

MEME_API_URL = "https://meme-api.com/gimme/wholesomememes"

app = Flask(__name__)


@app.route("/")
def index():
    response = requests.request("GET", MEME_API_URL, timeout=10)
    response.raise_for_status()
    meme = response.json()
    return render_template(
        "memes.html",
        meme_url=meme["url"],
        subreddit=meme["subreddit"],
    )


if __name__ == "__main__":
    app.run(debug=True)

