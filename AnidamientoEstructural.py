'''
AnidamientoEstructural.py
    script en Python que simula un juego de preguntas y respuestas, si el usuario
    contesta correctamente una pregunta puede continuar con la siguiente, en caso
    de fallar se le indica que ha perdido. Si contesta acertadamente todas las pre-
    guntas se le felicita por su conocimiento.
'''

print('Bienvenid@. Pongamos a prueba tu conocimiento')

respuesta = int(input('¿Cuál es la velocidad de la luz en m/s?: '))
if respuesta == 299792458:
    print('Correcto!')
    respuesta = int(input('¿Cuánto es 8+8/8*8?: '))
    if respuesta == 8+8/8*8:
        print('Correcto!')
        respuesta = input('¿De qué color eran las mangas del chaleco de Napoleón?: ')
        if respuesta == 'Los chalecos no tienen mangas':
            print('Correcto! Has contestado todo correctamenta!')
        else:
            print('Incorrecto, sigue intentando...')
    else:
        print('Incorrecto, sigue intentando...')
else:
    print('Incorrecto, sigue intentando...')
