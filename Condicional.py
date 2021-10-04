'''
Condicional.property
    script en Python que genera un número aleatorio entre 1 y 10 y le pida al
    usuario que intente adivinarlo. Si adivina el número que lo felicite por
    su logro
'''

import random

secreto = random.randint(1, 10)

print('Acabo de generar un número aleatorio entre 1 y 10. Intenta adivinar qué número es')
numero = int(input('¿Qué número crees que es?: '))

if numero == secreto:
    print('Felicidades, has adivinado en número crack')
else:
    print(f'Incorrecto, era: {secreto}')
