from flask import Flask
import random   

guess=random.randint(0,9)

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="gif">'

@app.route('/<int:number>')
def guess_number(number):
    
    if number > guess:  
        return '<h1>Too high,try again!</h1>' \
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="gif">'
    elif number < guess:
        return '<h1>Too low,try again!</h1>' \
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="gif">'
                
    else:
        return '<h1>You found me!</h1>' \
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="gif">'

if __name__ == '__main__':
    app.run(debug=True)
                  