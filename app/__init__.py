from flask import Flask

from config import Config
from app.extensions import db, lm

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Extensions
    db.init_app(app)
    lm.init_app(app)

    # Register blueprints here
    from app.main import main
    app.register_blueprint(main)
    from app.account import account
    app.register_blueprint(account)

    with app.app_context():

        from app.models.account import Account
        from flask_login import current_user
        
        # REMOVE LATER
        db.drop_all()
        db.create_all()
        # ***********

        @lm.user_loader
        def load_user(user_id):
            return Account.query.get(int(user_id))

        user = Account(
            first_name="Ed",
            last_name="Haig-Thomas",
            email="ed",
            passphrase=None
        )
        user.hash_passphrase("a")
        db.session.add(user)
        db.session.commit()

    return app



