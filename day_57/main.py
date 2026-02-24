from flask import Flask, render_template
import requests

# Get data
response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
response.raise_for_status()
data = response.json()

# Server
app = Flask(__name__)

@app.route('/')
def home():
    for post in data:
        match post["id"]:
            case 1:
                blog1 = post["title"]
                subtitle1 = post["subtitle"]
            case 2:
                blog2 = post["title"]
                subtitle2 = post["subtitle"]
    return render_template("index.html", blog1=blog1, subtitle1=subtitle1, blog2=blog2, subtitle2=subtitle2)

@app.route("/post/<id>")
def post(id):
    id = int(id)
    title = data[id-1]["title"]
    subtitle = data[id-1]["subtitle"]
    body = data[id-1]["body"]
    return render_template("post.html", title=title , subtitle=subtitle , body=body)

if __name__ == "__main__":
    app.run(debug=True)
