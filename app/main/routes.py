from app.main import main
from flask import render_template, request, url_for, redirect, flash
from flask_login import current_user, login_user

@main.route('/')
def index():

    if current_user.is_authenticated:
        user = current_user.first_name
    else:
        user = False

    return render_template('index.html', name=user)
