def data(x):
    data = []
    for i in range(1,x+1):
        data.append({
            'nom':f"nom complet {i}",
            'telephone' : f"+221 77 {i*100} {i*10} {i*10}",
            'mail' : f"mail{i}@gmail.com"
        })
    return data[1-1:5]

print(data(16))