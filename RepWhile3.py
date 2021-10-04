'''
RepWhile3.py
    script en Python que implemente el juego de adivinar un número, pero esta vez
    en modo competitivo. La computadora deberá generar un número aleatorio entre
    1 y 100 y tanto el usuario como la computadora deberán intentar adivinar dicho
    número. Para que el juego sea retador el jugador máquina deberá ser "inteligente"
    y competir para ganar. El juego se realizará por turnos, primero la máquina y
    después el usuario y por cada intento la computadora responderá si el número es
    mayor o menor que el secreto.
'''

import os
import random

secret = random.randint(1, 100)
user = -1
bot = -1
inf = 1
sup = 100

while user != secret and bot != secret:
    os.system('cls')
    print('Bot, ¿cuál crees que es el número secreto?: ')
    bot = random.randint(inf, sup)
    print(f'El Bot seleccionó: {bot}')
    if bot < secret:
        print('El número de Bot es menor')
        inf = bot + 1
    elif bot > secret:
        print('El numero de Bot es mayor')
        sup = bot - 1
    else:
        print('El Bot ha ganado')
    if bot != secret:
        user = int(input('Usuario, ¿cuál crees que es el número secreto?: '))
        if user < secret:
            print('Tu número es menor')
            if user > inf:
                inf = user + 1
        elif user > secret:
            print('Tu número es mayor')
            if user < sup:
                sup = user - 1
        else:
            print('Has adivinado el número')
    input('Presiona enter para continuar...')
