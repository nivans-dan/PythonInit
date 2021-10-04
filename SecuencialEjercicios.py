'''
SecuencialEjercicios.property
    script en Python que calcule el área de un triángulo. El usuario deberá ingresar
    el valor de la base como el de la altura y el programa mostrará el valor del área
'''

base = int(input('Dame la base del triángulo: '))
altura = int(input('Dame la altura del triángulo: '))
area = base * altura / 2
print(f'El área es: {base} x {altura} / 2 = {area}')
