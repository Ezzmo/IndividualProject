from application import db, login_manager
from flask_login import UserMixin

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    title = db.Column(db.String(100), nullable=False, unique=True)
    content = db.Column(db.String(500), nullable=False, unique=True)

    def __repr__(self):
        return ''.join([
            'User: ', self.first_name, ' ', self.last_name, '\r\n',
            'Title: ', self.title, '\r\n', self.content
            ])
@login_manager.user_loader
def load_user(username):
    return Users.query.get(Username=username)
class Users(db.Model, UserMixin):
    Username = db.Column(db.String(15), primary_key = True)
    Password = db.Column(db.String(30), nullable = False)
    Email = db.Column(db.String(50), nullable = False)

    def __repr__(self):
        return''.join(['Username: ', self.Username, '\r\n', 'Email: ', self.Email])

class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50), nullable=False, unique=True)
    Club = db.Column(db.String(50), nullable = False)
    League = db.Column(db.String(50), nullable = False)
    Position = db.Column(db.String(4), nullable = False)
    Tier = db.Column(db.String(6))
    Rating = db.Column(db.Integer)
    Pace = db.Column(db.Integer)
    Shooting = db.Column(db.Integer)
    Passing = db.Column(db.Integer)
    Dribbling = db.Column(db.Integer)
    Defending = db.Column(db.Integer)
    Physical = db.Column(db.Integer)

    def __repr__(self):
        return ''.join(['Name: ', self.Name, '\r\n', 'Club: ', self.Club, '\r\n', 'Position: ', self.Position])
