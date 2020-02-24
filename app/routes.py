from flask import render_template
from app import app

@app.route('/')
@app.route('/home')
def home():
    user = {'username': 'Mo'}
    posts =[
            {'author' : {'username' : 'Chief'},
             'body' : 'Anyone wanna play me?'
            },
            {'author' : {'username' : 'Merkleman'},
             'body' : 'Im definitely the best'
            }     
        ]
    return render_template('home.html', title='Home', user=user, posts=posts)

