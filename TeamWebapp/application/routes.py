from application import app, db, bcrypt
from flask import render_template, redirect, url_for, request, flash
from application.forms import *
from application.models import *
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home():
	players=Players.query.all()
	return render_template('home.html', title='Home', players=players)

@app.route('/account', methods=['GET', 'POST'])
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

@app.route('/community', methods=['GET', 'POST'])
def community():
	communityteams=UserTeams.query.all()
	return render_template("community.html", communityteams=communityteams)
@app.route('/editor', methods=['GET', 'POST'])
def editor():
	form = TeamEditor()
	form.club.choices = [(Players.Name,Players.Name) for Name in (Players.query.filter_by(League='England Premier League').all()]
	return render_template("editor.html", form = form)
@app.route("/account/delete", methods=["GET", "POST"])
@login_required
def account_delete():
        user = current_user.Username
        teams = UserTeams.query.filter_by(User=user).all()
        for team in teams:
                db.session.delete(team)
        account = Users.query.filter_by(Username=user).first()
        logout_user()
        db.session.delete(account)
        db.session.commit()
        return redirect(url_for('register'))
@app.route("/register", methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		user = Users(
			Username = form.username.data,
			Email = form.email.data,
			Password = bcrypt.generate_password_hash(form.password.data)
		)
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('home'))
	return render_template("register.html", form = form)