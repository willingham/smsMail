from app import app, db, models, login_manager
from flask import render_template, g


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
        user = models.User.query.get(form.email.data)
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                user.isAuthenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                return redirect(url_for('app.home'))
    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    user = current_user
    user.isAuthenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return render_template("logout.html")
