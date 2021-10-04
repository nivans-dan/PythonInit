'''
CondMult.py
    script en Python que solicite al usuario una calificación y una cantidad de
    asistencias a un curso. Si la calificación y la cantidad de asistencias son
    aprobatorias entonces se le felicita por su logro; en caso contrario, se le
    indicará en qué falló. La calificación mínima aprobatoria será de 60 y la
    cantidad mínima de asistencias será de 24.
'''

calMin = 60
asisMin = 24

cal = int(input('Dame tu calificación: '))
asis = int(input('Dame tus asistencias: '))

if cal >= calMin and asis >= asisMin:
    print('Felicidades, aprobaste el curso')
elif cal < calMin and asis >= asisMin:
    print(f'Calificación insuficiente, el mínimo es: {calMin}')
elif cal >= calMin and asis < asisMin:
    print(f'Asistencias insuficientes, el mínimo es: {asisMin}')
else:
    print(f'Calificación y asistencias insuficientes, los mínimos son: {calMin} y {asisMin}')
