import unittest 
from flask import url_for
from flask_testing import TestCase
from application.models import Review, Players
from application import app, db

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI= 'mysql+pymysql://root:rootpassword123@34.89.101.184/test', SECRET_KEY= '123456789', DEBUG=True)
        return app
    def setUp(self):
        db.create_all()
        review = Review(review= 'Excellent pace and a great eye for goal')
        player1 = Players(player= 'Mohamed Salah, Attacker, Liverpool: ')
        db.session.add(review)
        db.session.add(player1)
        db.session.commit()
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_index_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)

    def test_add_get(self):
        response = self.client.get(url_for('add', review_id=1))
        self.assertEqual(response.status_code, 200)

    def test_update_get(self):
        response = self.client.get(url_for('update', review_id=1))
        self.assertEqual(response.status_code,200)

    def test_delete_get(self):
        response = self.client.get(url_for('delete', review_id=1))
        self.assertEqual(response.status_code,302)