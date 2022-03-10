from importlib.resources import path
from flask import Flask
import random


app = Flask(__name__)
path = 'template.html'

@app.route('/')
def index():
    return '<h1>Hi Jord</h1>'

@app.route('/acceuil')
def acceuil():
    return '<ul><li>jord</li><li>rema</li></ul>'

@app.route('/nom_latin/<name>')
def changeName(name):
    nom_latin = ''
    if (name[-1]=='y'):
        nom_latin = name.replace(name[-1], 'iful')
    else:
        nom_latin = name+'y'
    return f"le nom en latin est  {nom_latin}"

#cours 2
from flask import render_template

@app.route('/template/')
def template():
    L = []
    for i in range(1, 10):
        nom = f"nom{i}"
        mail = f"maiil{i}@gmail.com"
        age = random.randint(5, 10)
        L.append([nom,mail, age])
    liste = ['jord', 'winiga', 'light']
    return render_template(path,
                           name="Jordan",
                           age=10,
                           tblName = liste)

@app.route('/test/<nom>/<myAge>')
def template2(nom, myAge):
    return render_template(path, name = nom, age = myAge)


#devoir cours 2 (à rendre au cours 3)

from db import users 
def generateData(x):
    data = []
    for i in range(1,x+1):
        data.append({
            'id' : i,
            'nom':f"nom complet {i}",
            'telephone' : f"+221 77 {i*100} {i*10} {i*10}",
            'mail' : f"mail{i}@gmail.com"
        })
    return data



@app.route('/template/pagination/<int:page>')
def pagination(page):
    #data = generateData(17)
    data = users
    table = []
    #page = int(page)
    indexPagination = len(data)//5+2
    if (page==1):
        table = data[0:5]
    else:
        if(page*5 < len(data)):
            table = data[((page-1)*5):page*5]
        else:
            table = data[((page-1)*5)::]
    return render_template('devoir.dictionnaire.html',data=table, indexPagination = indexPagination)

#cours 3

@app.route('/template/heritage/base')
def base():
    return render_template('./heritage/base.html')

@app.route('/template/heritage/home')
def home():
    return render_template('./heritage/home.html')


if __name__ == '__main__':
    app.run(debug=True)
