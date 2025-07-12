from app.extensions import db
from flask_login import UserMixin
import bcrypt

class Account(UserMixin, db.Model):
    """The Account model is for storing account information such as:
           First Name : string(50)
           Last Name : string(50)
           Email address : string(30)
           Hashed Passphrase : large binary
    """
    __tablename__ = "Account"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(254), nullable=False)
    passphrase = db.Column(db.LargeBinary, nullable=True)

    def hash_passphrase(self, passphrase: str) -> None:
        """Hashes the passphrase and stores it."""
        self.passphrase = bcrypt.hashpw(passphrase.encode('utf8'), bcrypt.gensalt())
        db.session.commit() # save passphrase to db

    def validate_passphrase(self, passphrase: str) -> bool:
        """Checks if the provided passphrase matches the stored hash."""
        print(f"ph: {passphrase.encode('utf8')}\nphh: {self.passphrase}")
        return bcrypt.checkpw(passphrase.encode('utf8'), self.passphrase)

    def __repr__(self):
        """How should this account entry be depicted as a string."""
        return f'<Account from "{self.first_name} {self.last_name}">'
