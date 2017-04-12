from getpass import getpass
import sys

from flask import current_app
from app import app, db, bcrypt
from app.models import User


def main():
    with app.app_context():
        db.metadata.create_all(db.engine)
        if User.query.all():
            create = input('A user already exists! Create another? (y/n)?')
            if create == 'n':
                return
        email = input('Enter email: ')
        smsEmail = input('Enter smsEmail address: ')
        password = getpass()
        assert password == getpass('Password (again):')
        user = User(email=email, password=bcrypt.generate_password_hash(password), smsEmail=smsEmail)
        db.session.add(user)
        db.session.commit()
        print('User added.')


if __name__ == '__main__':
    main()
            
