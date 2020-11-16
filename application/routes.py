from flask import render_template, redirect, url_for, request

from application import app, db
from application.models import Players, Review
from application.forms import ReviewForm

@app.route('/', methods= ['POST', 'GET'])
def index():
    all_players = Players.query.all()
    all_reviews = Review.query.all()
    return render_template('index.html', all_players=all_players, all_reviews=all_reviews)

@app.route('/add', methods= ['GET', 'POST'])
def add():
    form = ReviewForm()
    all_players = Players.query.all()
    player_choices = []
    for player in all_players:
        player_choices.append((str(player.id), player.player))
    form.playerid.choices = player_choices
    if form.validate_on_submit():
        new_review = Review(review=form.review.data, players_id=form.playerid.data)
        db.session.add(new_review)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.route('/update/<int:review_id>', methods= ['GET', 'POST'])
def update(review_id):
    form = ReviewForm()
    all_players = Players.query.all()
    player_choices = []
    for player in all_players:
        player_choices.append((str(player.id), player.player))
    form.playerid.choices = player_choices
    review_to_update = Review.query.get(review_id)
    if form.validate_on_submit():
        review_to_update.review = form.review.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.review.data = review_to_update.review
    return render_template('update.html', form=form)

@app.route('/delete/<int:review_id>')
def delete(review_id):
    review_to_delete = Review.query.get(review_id)
    db.session.delete(review_to_delete)
    db.session.commit()
    return redirect(url_for('index'))


