import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "4uh4iu62x3y4nudyehwduyi34hjdu4hjbrfktjrebknd" """os.environ.get('FLASK_SECRET_KEY')"""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
