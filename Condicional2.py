'''
Condicional2.py
    script en Python que implemente un sistema de redondeo de calificaciones. El usuario
    es el encargado de ingresar su calificación. Si a la calificación le faltan 4 unidades
    o menos para el siguiente múltiplo de 10, entonces su calificación será redondeada al
    siguiente múltiplo de 10, en caso contrario la calificación no es modificada.

    Ejemplo:

    Si el usuario obtuvo 76 entonces se redondea a 80
    Si el usuario obtuvo 77 entonces se redondea a 80
    Si el usuario obtuvo 75 entonces se redondea a 85
'''

calf = int(input('Dame tu calificación (del 10 al 100): '))
resd = calf % 10

if resd >= 6:
    calf = calf + (10 - resd)

print(f'Tu calificación final por redondeo es de: {calf}')
