from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

from application.models import Players, Review

class ReviewCheck:
    def __init__(self, message):
        self.message = message

    def __call__(self, form, field):
        all_reviews = Review.query.all()
        for review in all_reviews:
            if review.review == field.data:
                raise ValidationError(self.message)

class ReviewForm(FlaskForm):
    playerid = SelectField('Player',
                choices=[]
                )
    review = StringField('Review',
                validators=[
                    DataRequired()])
    submit = SubmitField('Add Review')
