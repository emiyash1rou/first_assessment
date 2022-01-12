from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(150),unique=True)
    username=db.Column(db.String(150),unique=True)
    firstname=db.Column(db.String(150))
    lastname=db.Column(db.String(150))
    password= db.Column(db.String(150))
    date_created= db.Column(db.DateTime(timezone=True),default=func.now())
    lastname=db.Column(db.String(150))
    todolists=db.relationship('ToDoList',backref='user',passive_deletes=True)
    admin=db.Column(db.String(150))
    # reference all the todolists references that user created
    #backref is from list how to access the user. 
class ToDoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.Text,nullable=False)
    description=db.Column(db.Text,nullable=False)
    date_created= db.Column(db.DateTime(timezone=True),default=func.now())
    author= db.Column(db.Integer,db.ForeignKey('user.id',ondelete="CASCADE"),nullable=False)


