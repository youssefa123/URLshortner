import random
import string
from flask import Flask, render_template, redirect, request, url_for


app = Flask(__name__)
shortened_urls = {}  # Corrected spelling

def generate_short_url(length=6):
    chars = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(chars) for _ in range(length))
    return short_url

# Removed space in route path and corrected the syntax for defining the route function
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        long_url = request.form['long_url']
        short_url = generate_short_url()
        while short_url in shortened_urls:  # Corrected spelling
            short_url = generate_short_url()

        # Indentation corrected; moved the dictionary update and return statement outside of the loop
        shortened_urls[short_url] = long_url  # Corrected spelling
        return f"Shortened URL: {request.url_root}{short_url}"
    else:
        # Corrected to ensure it always returns the template on a GET request
        return render_template("index.html")

@app.route("/<short_url>")
def redirect_url(short_url):
    long_url = shortened_urls.get(short_url)  # Corrected spelling
    if long_url:
        return redirect(long_url)
    else:
        return "URL NOT FOUND", 404

if __name__ == "__main__":
    app.run(debug=True, port=5001)

