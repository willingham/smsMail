from app import app, db, models, login_manager, bcrypt
from flask import render_template, redirect, url_for, flash, g
from flask_login import login_required, login_user, logout_user, current_user
from app.forms import LoginForm


@login_manager.user_loader
def user_loader(user_id):
    return models.User.query.get(user_id)


@app.before_request
def before_request():
    g.user = current_user


@app.route('/')
def index():
    users = models.User.query.all()
    user = g.user
    print('current user: ', user)
    return render_template('index.html', title='Home', user=user, users=users)


@app.route('/login', methods=['GET', 'POST'])
def login():
    print(db)
    form = LoginForm()
    if form.validate_on_submit():
        print(form.email.data)
        print(form.password.data)
        user = models.User.query.filter_by(email=form.email.data).first()
        if user:
            print("user found")
            if bcrypt.check_password_hash(user.password, form.password.data):
                print("###################33 user is authenticated.")
                user.isAuthenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                flash("Login Successful!", "success")
                return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout', methods=['GET'])
@login_required
def logout():
    user = current_user
    user.isAuthenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect(url_for("index"))


@app.route('/users', methods=['GET'])
@login_required
def users():
    users = models.User.query.all()
    return render_template("users.html", users=users)
