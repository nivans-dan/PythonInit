'''
RepWhile2.py
    script en Python que simule el sistema de validación de datos de una plataforma
    digital. Se le solicitará al usuario su nombre y contraseña mientras la información
    proporcionada no coincida con la información previamente registrada.
'''

import os

user = "Nivans_dan"
password = "asd123"
us = ''
pw = ''

while user != us or password != pw:
    os.system('cls')
    print('                     kiT-koT')
    us = input('Usuario: ')
    pw = input('Contraseña: ')

    if user != us or password != pw:
        print('Datos incorrectos')
        print('Intenta de nuevo')
        input('Presiona enter para continuar...')
    else:
        print('Bienvenid@')
