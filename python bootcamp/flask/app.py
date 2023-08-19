from flask import Flask

app = Flask(__name__)

def makebold(function):
    def wrapper_bold(*args, **kwargs):
        return "<b>" + function(*args, **kwargs) + "</b>"
    return wrapper_bold

def make_emphasis(function):
    def wrapper_em(*args, **kwargs):
        return "<em>" + function(*args, **kwargs) + "</em>"
    return wrapper_em

def make_underline(function):
    def wrapper_ul(*args, **kwargs):
        return "<u>" + function(*args, **kwargs) + "</u>"
    return wrapper_ul

@app.route("/")
@makebold
@make_emphasis
@make_underline
def hello():
    return "Hello World!"

@app.route("/users/<name>/<int:number>")
@make_underline
@makebold
@make_emphasis
def greet(name, number):
    return f"<h1>Hello {name}, your lucky number is {number}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
