import webbrowser
import sys
import random
import os 
import json

dir_path = os.path.dirname(os.path.realpath(__file__))
opcion=sys.stdin.read()

# print(dir_path)
with open(dir_path+'/canciones.json') as f:
  data = json.load(f)


if (opcion == 'aleatorio'):
    cantante = round((len(data)-1) * random.random())
    cancion = round(len( data[cantante]) * random.random())
    print('el cantante seleccionada es',data[cantante]["nombre"])
    print('la cancion ',cancion)
    webbrowser.open_new_tab(data[cantante]["canciones"][cancion])
else:
    for nombre in data:
        if opcion ==nombre["nombre"]:
            # print(nombre["canciones"])
            cancion = round((len( nombre["canciones"] )-1) * random.random())
            print('la cancion ',cancion)
            webbrowser.open_new_tab(nombre["canciones"][cancion])