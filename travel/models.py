from datetime import datetime
from enum import unique
from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, nullable=True)
    emailid = db.Column(db.String(100), unique=True, index=True, nullable=True)

    password_hash = db.Column(db.String(255), nullable=False)

    # uppercase foreign key class
    comments = db.relationship('Comment', backref='user')

class Destination(db.Model):
    __tablename__ = 'destinations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(400))
    image = db.Column(db.String(400))
    currency = db.Column(db.String(400))

    # uppercase foreign key class
    comments = db.relationship('Comment', backref='destination')

    def __repr__(self):
        str = 'Name {0} , Currency {1}, Description {2}, Image url {3}, Currency {4}'
        str.format(self.name, self.currency, self.description, self.image, self.currency)
        pass

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now)

    # foreign keys
    user_id= db.Column(db.Integer, db.ForeignKey('users.id'))
    destination_id= db.Column(db.Integer, db.ForeignKey('destinations.id'))

    def __repr__(self):
        str = 'User {0} , \n Text {1}'
        str.format(self.user, self.text)
        return str
        

