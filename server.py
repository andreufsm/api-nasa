import requests

astronautas = requests.get('http://api.open-notify.org/astros.json')
astronautas_json  = astronautas.json()
print("Atualmente existem %s astronautas no espaço \n" % (astronautas_json['number']))

for a in astronautas_json['people']:
    print("Astronauta: %s " % (a['name']))