from flask import Flask
from random import randint

# Random number
ranint = randint(0,9)

# Decorator
def decorator(func):
    def wrapper(**kwargs):
        func(kwargs)
        if kwargs['number'] == ranint:            
            result = '<h1 style="color:green">You Find Me</h><br>' \
    '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/>'
        elif kwargs['number'] > ranint:
            result = '<h1 style="color:red">Too high</h><br>' \
    '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"/>'
        else:
            result = '<h1 style="color:blue">Too low</h><br>' \
    '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"/>'
        return result
    return wrapper

# Flask server
app = Flask(__name__)

@app.route("/")
def root():
    return '<h1>Guess a number between 0 and 9</h><br>' \
    '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExeHdyY3RlOGV5Z3djcGN0ZTlzZHphMTBmcWlyd3Ywd3oxMXd3cDZmbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HXIiPZ2v60oM9e5LyH/giphy.gif"/>'

@app.route("/<int:number>")
@decorator
def guess(number):
    return ''

if __name__ == "__main__":
    app.run(debug=True)