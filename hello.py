import random

saludos = {'esp':'Hola mundo!','eng':'Hello world!','por':'Olá mundo!','ger':'Hallo welt!','fra':'Salut monde!','ita':'Ciao mondo!'}

print(saludos[random.choice(list(saludos.keys()))])