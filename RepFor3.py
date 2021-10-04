'''
RepFor3.py
    script en Python que muestre la tabla de multiplicar de un número ingresado
    por el usuario. El usuario tambipen podrá ingresar hasta qué valor llegará
    la tabla de multiplicar.
'''

num = int(input('¿De qué número deseas ver la tabla de multiplicar?: '))
lim = int(input('¿Hasta qué múltiplo deseas ver?: '))

print(f'                Tabla del número {num}')
for mult in range(1, lim + 1):
    print(f'{num} x {mult} = {num * mult}')
