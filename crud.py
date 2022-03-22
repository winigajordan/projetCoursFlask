from app import db, User

'''
create

elise = User("Rose Elise", "AKLOYO", 19)
yamine = User("Yamine", "IDISSA", 20)

#Ajout
db.session.add_all([elise,yamine])
db.session.commit()
'''


'''
Read
'''
#lecture par id
ob_selected = User.query.get(1) #select * from User where id=1
data = User.query.all()#select * from User
ob_filter = User.query.filter_by(firstName = "IDISSA").first()

#print(User.query.get(1))


'''
UPDATE
'''
ob_updt = User.query.get(1)

ob_updt.age=12
db.session.add(ob_updt)
db.session.commit()




'''
DELETE
'''
print(User.query.all())
ob_del = User.query.get(2)
db.session.delete(ob_del)
db.session.commit
print(User.query.all())
