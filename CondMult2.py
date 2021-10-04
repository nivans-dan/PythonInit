'''
CondMult2.py
    script en Python que muestre un menú con los nombres de distintos países de
    América y si el usuario selecciona alguna de las opciones se le mostrará el
    nombre de la capital de ese país
'''

mex = 1
uru = 2
col = 3
arg = 4
ecu = 5
per = 6

print('''           Capitiales de América
1) México
2) Uruguay
3) Colombia
4) Argentina
5) Ecuador
6) Perú
''')

opc = int(input('Dame el número del país del cual quieres saber su capital: '))

if opc == mex:
    print('Ciudad de México')
elif opc == uru:
    print('Montevideo')
elif opc == col:
    print('Bogotá')
elif opc == arg:
    print('Buenos Aires')
elif opc == ecu:
    print('Quito')
elif opc == per:
    print('Lima')
else:
    print('No está disponible ese número. Vuelve a intentar')
