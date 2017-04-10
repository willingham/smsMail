from app import app, db, models
from flask import render_template

@app.route('/')
def home():
    users = models.User.query.all()
    return render_template('home.html', title='Home', users=users)
