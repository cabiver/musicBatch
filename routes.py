import webbrowser
import sys
import random
# import random
opcion=sys.stdin.read()

listaNombre =[
    'persona',
    'bayonetta',
    'caleb',
    'cg5',
    'jonathan yong'
]
listaDeCantantes =[
    [
        'https://www.youtube.com/watch?v=qk0J9b4BEqY&list=RDqk0J9b4BEqY&start_radio=1',
        'https://www.youtube.com/watch?v=bbFO-pw4gAM',
        'https://www.youtube.com/watch?v=0jm8nnHqx80',
        'https://www.youtube.com/watch?v=vWWy7V9rCrA',
        'https://www.youtube.com/watch?v=HU_Z8RKo_Ow&t=17s',
        'https://www.youtube.com/watch?v=_F6LD_czS8s'
    ],
    [
        'https://www.youtube.com/watch?v=EV6E13xODyA',
        'https://www.youtube.com/watch?v=sXhhdNL05sY',
        'https://www.youtube.com/watch?v=5HcmhgGp9QQ',
        'https://www.youtube.com/watch?v=TMerSyvVarc'
    ],
    [
        'https://www.youtube.com/watch?v=PUllEnsZ5IM',
        'https://www.youtube.com/watch?v=Hj5Konof0gI',
        'https://www.youtube.com/watch?v=gcipipADLnw',
        'https://www.youtube.com/watch?v=doWygi9e5L8'
    ],
    [
        'https://www.youtube.com/watch?v=U1NmdJbTpQI',
        'https://www.youtube.com/watch?v=SXJGTnVfJic',
    ],
    [
        'https://www.youtube.com/watch?v=2RBazTfpybw',
        'https://www.youtube.com/watch?v=DiaVqBSs550'
    ]
]

if (opcion == 'aleatorio'):
    cantante = round((len(listaDeCantantes)-1) * random.random())
    print('la musica seleccionada es ',listaNombre[cantante])
    cancion = round(len( listaDeCantantes[cantante]) * random.random())
    print('la cancion ',cancion)
    webbrowser.open_new_tab(listaDeCantantes[cantante][cancion])
else:
    if opcion == 'persona':
        webbrowser.open_new_tab(listaDeCantantes[0][0])
    if(opcion == 'bayonetta'):
        webbrowser.open_new_tab(listaDeCantantes[1][0])



# def showVideo(persona, url):
#     if(opcion == persona):
#         webbrowser.open_new_tab(url)

# print("esto es lo que mando: "+opcion)

# showVideo('persona','https://www.youtube.com/watch?v=qk0J9b4BEqY&list=RDqk0J9b4BEqY&start_radio=1')
# showVideo('bayonetta','https://www.youtube.com/watch?v=yckWVQlt8Mo&list=RDyckWVQlt8Mo&start_radio=1')
# showVideo('dream','https://www.youtube.com/watch?v=SXJGTnVfJic')
# showVideo('evangelion','https://www.youtube.com/watch?v=6kguaGI7aZg')
# showVideo('caleb','https://www.youtube.com/watch?v=gcipipADLnw&list=RDMMyckWVQlt8Mo&index=2')
# showVideo('giveHearts','https://www.youtube.com/watch?v=wgNqW2gEDiY')




# persona = [
#     'https://www.youtube.com/watch?v=qk0J9b4BEqY&list=RDqk0J9b4BEqY&start_radio=1',
#     'https://www.youtube.com/watch?v=bbFO-pw4gAM',
#     'https://www.youtube.com/watch?v=0jm8nnHqx80',
#     'https://www.youtube.com/watch?v=vWWy7V9rCrA',
#     'https://www.youtube.com/watch?v=HU_Z8RKo_Ow&t=17s',
#     'https://www.youtube.com/watch?v=_F6LD_czS8s'
# ]
# bayonetta = [
#     'https://www.youtube.com/watch?v=EV6E13xODyA',
#     'https://www.youtube.com/watch?v=sXhhdNL05sY',
#     'https://www.youtube.com/watch?v=5HcmhgGp9QQ',
#     'https://www.youtube.com/watch?v=TMerSyvVarc'
# ]
# caleb = [
#     'https://www.youtube.com/watch?v=PUllEnsZ5IM',
#     'https://www.youtube.com/watch?v=Hj5Konof0gI',
#     'https://www.youtube.com/watch?v=gcipipADLnw',
#     'https://www.youtube.com/watch?v=doWygi9e5L8'
# ]
# ch5 =[
#     'https://www.youtube.com/watch?v=U1NmdJbTpQI',
#     'https://www.youtube.com/watch?v=SXJGTnVfJic',

# ]
# jonathan_Young = [
#     'https://www.youtube.com/watch?v=2RBazTfpybw',
#     'https://www.youtube.com/watch?v=DiaVqBSs550'
# ]