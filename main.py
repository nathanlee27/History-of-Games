import data

from flask import Flask, render_template

#create a Flask instance
app = Flask(__name__)

#connects default URL to a function
@app.route('/')
def home():
    #Flask import uses Jinga to render HTML
    return render_template("home.html")
    
@app.route('/tetris/')
def tetris():
    return render_template("tetris.html", data=data.tetris())

@app.route('/mario/')
def mario():
    return render_template("mario.html", data=data.mario())

@app.route('/hangman/')
def hangman():
    return render_template("hangman.html", data=data.hangman())

@app.route('/pacman/')
def pacman():
    return render_template("pacman.html", data=data.pacman())

@app.route('/playground/')
def playground():
    return render_template("playground.html", datalist=data.playlist())

@app.route('/monkey/')
def monkey():
    return render_template("monkey.html", data=data.monkey())

if __name__ == "__main__":
    app.run(debug=True, port='5002', host='127.0.0.1')