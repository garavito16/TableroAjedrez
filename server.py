from distutils.debug import DEBUG
from distutils.log import debug
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_board():
    return render_template("index.html",x=8,y=8,first_color="Black",second_color="Red")

@app.route('/<int:y>')
def show_board_row(y):
    return render_template("index.html",x=8,y=y,first_color="Black",second_color="Red")

@app.route('/<int:y>/<int:x>')
def show_board_row_column(y,x):
    return render_template("index.html",x=x,y=y,first_color="Black",second_color="Red")

@app.route('/<int:y>/<int:x>/<string:first_color>')
def show_board_row_column_color(y,x,first_color):
    return render_template("index.html",x=x,y=y,first_color=first_color,second_color="Red")

@app.route('/<int:y>/<int:x>/<string:first_color>/<string:second_color>')
def show_board_row_column_colors(y,x,first_color,second_color):
    return render_template("index.html",x=x,y=y,first_color=first_color,second_color=second_color)

if __name__ == '__main__':
    app.run(debug==True)