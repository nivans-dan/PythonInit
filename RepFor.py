'''
RepFor.py
    script en Python que imprima los números pares desde el 2 hasta el 20 haciendo
    uso de un ciclo For.
'''

print('             Programa que muestra los números pares desde el 2 hasta el 20')

print('     Método 1')
for num in range(1, 11):
    print(f'Par: {num*2}')
print('*'*20)
print('     Método 2')
for num in range(1, 21):
    if num % 2 == 0:
        print(f'Par: {num}')
print('*'*20)
print('     Método 3')
for num in range(2, 21, 2):
    print(f'Par: {num}')
