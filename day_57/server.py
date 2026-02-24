from flask import Flask, render_template
import requests

# name Decorator
def gender_age_api(func):
    def wrapper(**kwargs):
        response = requests.get(url=f"https://api.genderize.io?name={kwargs["name"]}")
        response.raise_for_status()
        gender = response.json()["gender"]
        response = requests.get(url=f"https://api.agify.io?name={kwargs["name"]}")
        response.raise_for_status()
        age = response.json()["age"]
        func(kwargs)
        return render_template("guess.html", name=kwargs["name"], gender=gender, age=age)
    return wrapper

# Server
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/guess/<name>")
@gender_age_api
def guess(name):
    return

@app.route("/blog")
def blog():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_post = response.json()
    return render_template("blog.html", all_post=all_post)

if __name__ == "__main__":
    app.run(debug=True)