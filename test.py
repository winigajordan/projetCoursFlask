from logging import error


def data(x):
    data = []
    for i in range(1,x+1):
        data.append({
            'nom':f"nom complet {i}",
            'telephone' : f"+221 77 {i*100} {i*10} {i*10}",
            'mail' : f"mail{i}@gmail.com"
        })
    return data[1-1:5]

#print(data(16))


def verification(nom):
    minu = False
    maj = False
    num = False
    for i in nom:
        if (i.isupper()):
            maj = True
        elif(i.islower()):
            minu = True
    if (nom[-1].isdecimal()):
        num = True
    return  {"majuscule" : maj,"minuscule" : minu, "chiffre" : num }

def errors(login):
    error = ""
    if (login !=""):
        result = verification(login)
        if result["majuscule"] == False:
            error += "Il manque une lettre majuscule \n"
        if result["minuscule"] == False:
            error += "Il manque une lettre minuscule \n"
        if result["chiffre"] == False:
            error += "Il manque un chiffre \n"
        if (result["chiffre"] == True and result["majuscule"] == True and result["minuscule"]):
            error += "Votre login repond aux exigences \n"
    else:
        error += "Chaine vide"
    return error
