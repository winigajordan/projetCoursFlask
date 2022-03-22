from app import db, User

# creation de la base de donnée
db.create_all()

# création des utilisateurs
jord = User("Jordan", "REMA", 19)
junior = User("Junior", "ADANHODOU", 20)
esse = User("Esse Jacques", "DANSOMON", 18)
steno = User("Stephane", "AKOLATSE", 21)

# affichage des id avant insertion
print(jord.id)
print(junior.id)
print(steno.id)

#mettre les objets dans la memoire tampon
db.session.add(jord)
db.session.add(junior)
db.session.add(esse)
db.session.add(steno)

#inserer dans la base
db.session.commit()

#affichage des id apès insertion
print(jord.id)