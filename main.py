# AULA TIRA DÚVIDAS TRAINEE SISTEMAS EMBARCADOS
# PROF. JEFFERSON SILVA
# 29/08/2020
# jeffersonsilva@lapisco.ifce.edu.br

import json
from firebase import firebase

from random import randint
import time

cont = 0

while True:
    temp = randint(25, 31)  # sensor de temperatura em graus celsius
    rpm = randint(50, 60)  # sensor de RPM
    vel = randint(40, 60)  # velocidade de um veiculo em km/h
    lux = randint(0, 10)  # sensor de luminosidade em lux

    t = str(temp)
    r = str(rpm)
    v = str(vel)
    l = str(lux)

    json_data = {'a': t, 'b': r, 'c': v, 'd': l}  # dictionary
    json_data = json.dumps(json_data, indent=4, sort_keys=True)  # convert dict to string and sort

    parsed_json = (json.loads(json_data))
    print(json_data)

    # authentication e insert
    if cont==0:
        firebase = firebase.FirebaseApplication('https://teste01-80e98.firebaseio.com/', authentication=None)
        result = firebase.post('/', parsed_json)
        print(result)
    else:
        firebase.put('/', result['name'], parsed_json) # update

    time.sleep(2)
    cont += 1
