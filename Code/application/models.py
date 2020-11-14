from application import db

class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    review = db.relationship('Review', backref='players')
    
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rev = db.Column(db.String(255))
    rating = db.Column(db.Integer)
    players_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=True)
