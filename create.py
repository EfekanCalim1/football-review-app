from application import db 
from application.models import Players

db.drop_all()
db.create_all()

new_player = Players(player = "Mohamed Salah, Attacker, Liverpool: ")
db.session.add(new_player)
new_player = Players(player = "Sadio Mane, Attacker, Liverpool: ")
db.session.add(new_player)
new_player = Players(player = "Trent Alexander-Arnold, Defender, Liverpool: ")
db.session.add(new_player)
new_player = Players(player = "Kevin De Bruyne, Midfielder, Man City: ")
db.session.add(new_player)
new_player = Players(player = "Raheem Sterling, Attacker, Man City: ")
db.session.add(new_player)
new_player = Players(player = "Sergio Aguero, Attacker, Man City: ")
db.session.add(new_player)
new_player = Players(player = "Timo Werner, Attacker, Chelsea: ")
db.session.add(new_player)
new_player = Players(player = "Kai Havertz, Midfielder, Chelsea: ")
db.session.add(new_player)
new_player = Players(player = "Hakim Ziyech, Midfielder, Chelsea: ")
db.session.add(new_player)
new_player = Players(player = "Marcus Rashford, Attacker Man Utd: ")
db.session.add(new_player)
new_player = Players(player = "Bruno Fernandes, Midfielder, Man Utd: ")
db.session.add(new_player)
new_player = Players(player = "Paul Pogba, Midfielder, Man Utd: ")
db.session.add(new_player)
new_player = Players(player = "Hueng Min Son, Attacker, Spurs: ")
db.session.add(new_player)
new_player = Players(player = "Sergio Reguilon, Defender, Spurs: ")
db.session.add(new_player)
new_player = Players(player = "Jamie Vardy, Attacker, Leicester: ")
db.session.add(new_player)
new_player = Players(player = "Ben Chilwell, Defender, Chelsea: ")
db.session.add(new_player)
new_player = Players(player = "N'Golo Kante, Midfielder, Chelsea: ")
db.session.add(new_player)
new_player = Players(player = "Mason Mount, Midfielder, Chelsea: ")
db.session.add(new_player)
new_player = Players(player = "Thiago Silva, Defender, Chelsea: ")
db.session.add(new_player)
new_player = Players(player = "Jordan Henderson, Midfielder, Liverpool: ")
db.session.add(new_player)
new_player = Players(player = "Kurt Zouma, Defender, Chelsea: ")
db.session.add(new_player)
new_player = Players(player = "Edouard Mendy, Goalkeeper, Chelsea: ")
db.session.add(new_player)
new_player = Players(player = "Allison Becker, Goalkeeper, Liverpool: ")
db.session.add(new_player)
new_player = Players(player = "Ederson, Goalkeeper, Man City: ")
db.session.add(new_player)
new_player = Players(player = "Hugo Lloris, Goalkeeper, Spurs: ")
db.session.add(new_player)
new_player = Players(player = "David De Gea, Goalkeeper, Man Utd: ")
db.session.add(new_player)
new_player = Players(player = "Emiliano Martinez, Goalkeeper, Aston Villa: ")
db.session.add(new_player)
new_player = Players(player = "Jack Grealish, Midfielder, Aston Villa: ")
db.session.add(new_player)
db.session.commit()