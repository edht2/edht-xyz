from app.main import main
from flask import render_template, request, url_for, redirect, flash
from flask_login import current_user, login_user

@main.route('/')
def index():

    if not current_user.is_authenticated:
        return render_template('index.html')
    
    return render_template('home.html', name=current_user.first_name)

    


