from application import app, db, bcrypt
from flask import render_template, redirect, url_for, request
from application.forms import PostForm, RegistrationForm, LoginForm, UpdateAccountForm
from application.models import Posts, Users
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('account.html', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
	if form.validate_on_submit():
		current_user.first_name = form.first_name.data
		current_user.last_name = form.last_name.data
		current_user.email = form.email.data
		db.session.commit()
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.first_name.data = current_user.first_name
		form.last_name.data = current_user.last_name
		form.email.data = current_user.email
	return render_template('account.html', title='Account', form=form)

@app.route('community.html', methods=['GET', 'POST'])
def community():
	communityteams=UserTeams.query.all()