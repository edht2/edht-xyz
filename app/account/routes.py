from app.account import account
from app.account.validators import validate_signup
from flask import render_template, request, url_for, redirect, flash
from app.extensions import db
from app.models.account import Account
from flask_login import current_user, login_user, logout_user, login_required


@account.route('/signup', methods=['GET', 'POST'])
def signup():
    """ Sign-Up page - This will contain what you expect, a short form which is validated
    and then appended to the database, it also signs-in the user after the account has been added """


    if current_user.is_authenticated:
        # if the user is already signed in send them to index as they should be able to sign-up while signed in
        return redirect(url_for('main.index'))


    if request.method == 'POST':
        # when the sign-up form is submitted

        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        passphrase = request.form.get('passphrase')
        # get all of the form data

        results = validate_signup(first_name, last_name, email, passphrase)
        # validate the sign-up credentials

        if results["summary"]:
            # if the credentials were invalid
            results['first_name'] = first_name
            results['last_name'] = last_name
            results['email'] = email
            results['passphrase'] = passphrase
            
            flash(results)
            # send them back to client with an error message

        else:
            user = Account(first_name=first_name, last_name=last_name, email=email, passphrase=None)
            # create new account

            db.session.add(user)
            db.session.commit()
            # save the new account to the db

            user.hash_passphrase(passphrase)
            # hash and add the passphrase

            login_user(user)
            # login the user

            return redirect(url_for('main.index'))
            # send them to the home page!

    return render_template('signup.html')


@account.route('/signin', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        # if they are signed in
        return redirect(url_for('main.index'))

    if request.method == 'POST':
        # when the signin form is submitted
        email = request.form.get('email')
        passphrase = request.form.get('passphrase')

        account: Account = Account.query.filter_by(email=email).all()

        if account and account.validate_passphrase(passphrase):
            # check if the passphrase matches the email
            
            login_user(account, remember=True)
            # signin the user
            
            next_page = request.args.get('next')
            # find to the page they tried to access
            
            return redirect(next_page or url_for('main.index'))
            # take them to home or the page they were tring to access
        else:
            flash("Invalid passphrase-email combo")
            # alert the client it has failed
            
    return render_template('signin.html')

@login_required
@account.route('/signout')
def signout():

    logout_user()

    return redirect(url_for('main.index'))
