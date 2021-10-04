'''
RepWhile.py
    script en Python que sume valores pares y multiplique valores impares mientras
    el usuario no ingrese un 0. Se deberá utilizar la estrucutra repetitiva "mientras"
    para solicitar al usuario un número y dependiendo del número lo suma o lo mul-
    tiplica.
'''

sum = 0
mult = 1
opc = -1

while opc != 0:
    opc = int(input("Dame un número. Presiona 0 para salir: "))
    if opc % 2 == 0:
        sum = sum + opc
    else:
        mult = mult * opc

    print(f'Suma: {sum}')
    print(f'Multiplicación: {mult}')
