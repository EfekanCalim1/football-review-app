from flask import render_template, redirect, url_for, request

from application import app, db
from application.models import Players, Review
from application.forms import PlayersForm, ReviewForm

@app.route('/', methods= ['POST', 'GET'])
def index():
    all_players = Players.query.all()
    return render_template('index.html', all_players=all_players)

@app.route('/add', methods= ['GET', 'POST'])
def add():
    form = PlayersForm()
    if form.validate_on_submit():
        new_player = Players(name=form.name.data)
        player_team = Players(team=form.team.data)
        db.session.add(new_player)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.route('/update/<int:id>', methods= ['GET', 'POST'])
def update(id):
    form = PlayersForm()
    players_update = Players.query.get(id)
    if form.validate_on_submit():
        players_update.name = form.name.data
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', form=form)

@app.route('/delete/<int:id>')
def delete(id):
    players_delete = Players.query.get(id)
    db.session.delete(players_delete)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/addreview/<int:id>', methods= ['GET', 'POST'])
def add_review(id):
    form = ReviewForm()
    if form.validate_on_submit():
        new_review = Review(rev=form.rev.data, rating=form.rating.data, players_id=id)
        db.session.add(new_review)
        db.session.commit()
        return redirect(url_for('reviews', id=id))
    return render_template('addreview.html', form=form, players= Players.query.get(id))

@app.route('/reviews/<int:id>', methods=['GET', 'POST'])
def reviews(id):
    reviews = Review.query.filter_by(players_id=id).all()
    return render_template ('reviews.html', reviews=reviews)