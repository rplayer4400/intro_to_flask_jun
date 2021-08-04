from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import RegisterForm
from app.models import User

@app.route('/')
def index():
    name = 'Brian'
    title = 'Coding Temple Intro to Flask'
    return render_template('index.html', name=name, title=title)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        print(username, email, password)

        new_user = User(username, email, password)

        db.session.add(new_user)
        db.session.commit()

        flash(f'Thank you for signing up {new_user.username}!','primary')


        return redirect(url_for('index'))
        
    return render_template('register.html', title='Register for CT Blog', form=form)