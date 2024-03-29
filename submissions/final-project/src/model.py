from . import db

class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    website = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<Password {self.website}-{self.email}>'