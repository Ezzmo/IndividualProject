from flask import render_template, redirect, url_for
from application import app, db
from application.models import Posts
from application.forms import PostForm
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
@app.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        postData = Posts(
                first_name = form.first_name.data,
                last_name = form.last_name.data,
                title = form.title.data,
                content = form.content.data
            )
        db.session.add(postData)
        db.session.commit()

        return redirect(url_for('home'))
    else:
        print(form.errors)

    return render_template('post.html', title='Post', form=form)
@app.route('/board')
def board():
    posts = Posts.query.all()[::-1]
    return render_template('postboard.html', posts=posts)
