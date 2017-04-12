from app import app, db, models, login_manager, bcrypt
from flask import render_template, redirect, url_for, g
from flask_login import login_required, login_user
from app.forms import LoginForm


@login_manager.user_loader
def user_loader(user_id):
    return models.User.query.get(user_id)


@app.route('/')
def home():
    users = models.User.query.all()
    return render_template('home.html', title='Home', users=users)


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
                return redirect(url_for('home'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout', methods=['GET'])
@login_required
def logout():
    user = current_user
    user.isAuthenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return render_template("logout.html")
