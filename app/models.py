from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    smsEmail = db.Column(db.String)
    email = db.Column(db.String)
    lastName = db.Column(db.String)
    firstName = db.Column(db.String)
    isSender = db.Column(db.Boolean, default=False)
    isActive = db.Column(db.Boolean, default=True)
    isAuthenticated = db.Column(db.Boolean, default=False)
    password = db.Column(db.String)
    posts = db.relationship('Message', backref='author', lazy='dynamic')

    def __init__(self, email, smsEmail, password):
        self.email = email
        self.smsEmail = smsEmail
        self.password = password

    @property
    def is_authenticated(self):
        return self.isAuthenticated

    @property
    def is_active(self):
        return self.isActive

    @property
    def is_anonymous(self):
        return True

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<User %r>' % self.smsEmail


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Message %r>' % self.message
