import requests
import json


def georeference(n):
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    consulta = json.loads(response.text)
    lista = []
    n=(input("Ingrese un numero :"))
    nombre= (consulta[int(n)]['name'])
    lat = (consulta[int(n)]['address']['geo']['lat'])
    lng = (consulta[int(n)]['address']['geo']['lng'])
    lista.append([nombre,lat,lng])
    print(lista)
n=0
georeference(n)

