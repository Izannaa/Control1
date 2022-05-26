import requests 
import json

response = requests.get('https://randomuser.me/api')
consulta = json.loads(response.text)

def show():
    if (consulta['results'][0]['gender']) == "male":
        nombre=(consulta['results'][0]['name']['first'])
        apellido=(consulta['results'][0]['name']['last'])
        user=(consulta['results'][0]['login']['username'])
        contra=(consulta['results'][0]['login']['password'])
        print("\nHombre","\nNombre:",nombre ,"\nApellido:",apellido,"\nUser:",user,"\npassword:",contra)
    else:
        nombre=(consulta['results'][0]['name']['first'])
        apellido=(consulta['results'][0]['name']['last'])
        ciudad=(consulta['results'][0]['location']['city'])
        calle=(consulta['results'][0]['location']['street']['name'])
        ncalle=(consulta['results'][0]['location']['street']['number'])
        print("\nMujer","\nNombre:",nombre, "\nApellido:",apellido,"\nCiudad",ciudad,"\nCalle:",calle,"\nNumeroCalle:",ncalle,)

show()