from run import app
from models import Class
from forms import LoginForm
from flask import render_template

@app.route("/")
def home():
    return "<h1>My flask app!</h1>\n"

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('index.html', form=form)
