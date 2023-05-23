from flask import Flask, render_template
from model import Game, Player, Choice

app = Flask(__name__)

game = Game()

@app.route("/")
def hello_world():
    return render_template("game.html", game=game, player=Player)

@app.route("/r")
def reset():
    game.reset()
    return render_template("game.html", game=game, player=Player)

@app.route("/✋")
def play_paper():
    game.play(Choice.paper)
    return render_template("game.html", game=game, player=Player)

@app.route("/✊")
def play_rock():
    game.play(Choice.rock)
    return render_template("game.html", game=game, player=Player)

@app.route("/✌️")
def play_scissors():
    game.play(Choice.scissors)
    return render_template("game.html", game=game, player=Player)