from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime

class Players(db.Model):
    Name = db.Column(db.String(50), nullable=False, primary_key=True)
    Club = db.Column(db.String(50), nullable=False)
    League = db.Column(db.String(50), nullable=False)
    Position = db.Column(db.String(4), nullable = False)
    Rating = db.Column(db.Integer,nullable = False)

    def __repr__(self):
        return ''.join([
            self.Name, '\r\n',
            "Club: ",self.Club, '\r\n',
            "Position: ", self.Position, '\r\n',
            "Rating: ", str(self.Rating)
        ])
class Users(db.Model):
    Username = db.Column(db.String(50),primary_key=True)
    Email = db.Column(db.String(50),nullable=False)
    Password = db.Column(db.String(250), nullable=False)
    Teams= db.relationship("UserTeams", backref="Creator", lazy=True)

class UserTeams(db.Model):
    TeamID = db.Column(db.Integer, primary_key=True)
    TeamName = db.Column(db.String(50),nullable = False)
    Rating = db.Column(db.Integer, nullable = False)
    User = db.Column(db.String(50), db.ForeignKey(Users.Username))


    def __repr__(self):
        return ''.join([
            self.TeamName, '\r\n',
            "Rating: ", str(self.Rating), '\r\n'
            "Created by: ", self.User
        ])
class Lineups(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Player = db.Column(db.String(50), nullable=False)
    TeamId = db.Column(db.String(50), nullable=False)


@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))