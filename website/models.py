from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #referencing user.id like sql
    price = db.Column(db.Float)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') #use uppercase when rs but lowercase for foreign key
    portfolio = db.relationship('Portfolio')
    portfolioHistory = db.relationship('PortfolioHistory')

class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #referencing user.id like sql
    bought_price = db.Column(db.Float)
    bought_qty = db.Column(db.Float)
    current_price = db.Column(db.Float)
    profitloss = db.Column(db.Float) #floating profit loss

class PortfolioHistory(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    stock = db.Column(db.String(20))
    status = db.Column(db.String(10))
    qty_exchanged = db.Column(db.Float)
    bought_price = db.Column(db.Float)
    sold_price = db.Column(db.Float)
    profitloss = db.Column(db.Float)


