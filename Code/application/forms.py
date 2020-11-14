from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

from application.models import Players, Review

class PlayersCheck:
    def __init__(self, message):
        self.message = message

    def __call__(self, form, field):
        all_players = Players.query.all()
        for players in all_players:
            if players.name == field.data:
                raise ValidationError(self.message)

class PlayersForm(FlaskForm):
    name = StringField('Player Name',
                validators=[
                    DataRequired(),
                    PlayersCheck(message= 'You have already added this player')
                ]
            )
    team = StringField('Player Team', 
                validators=[
                    DataRequired()])
    submit = SubmitField('Add Player')

class ReviewForm(FlaskForm):
    rating = SelectField('Rating',
                choices=[
                    ('Ten', '10'), ('Nine', '9'), ('Eight', '8'), ('Seven', '7'), ('Six', '6'), ('Five', '5'), ('Four', '4'), ('Three', '3'), ('Two', '2'), ('One', '1'), ('Zero', '0')])
    rev = StringField('Review',
                validators=[
                    DataRequired()])
    submit = SubmitField('Add Review')
