from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    smsEmail = db.Column(db.String)
    email = db.Column(db.String)
    lastName = db.Column(db.String)
    firstName = db.Column(db.String)
    isSender = db.Column(db.Boolean, default=False)
    isActive = db.Column(db.Boolean, default=True)
    posts = db.relationship('Message', backref='author', lazy='dynamic')

    def __init__(self, smsEmail):
        self.smsEmail = smsEmail

    def __repr__(self):
        return '<User %r>' % self.smsEmail


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Message %r>' % self.message
