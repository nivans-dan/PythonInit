'''
SelecMult.py
    script en Python que simula una calculadora con las operaciones aritméticas básicas. El menú mostrado será el siguiente:

    1) Suma
    2) Resta
    3) Multiplicación
    4) División
    5) División Entera
    6) Módulo
    7) Potencia
'''

sum = 1
res = 2
mult = 3
div = 4
divEnt = 5
mod = 6
pot = 7

print('''             Calculadora
1) Suma
2) Resta
3) Multiplicación
4) División
5) División Entera
6) Módulo
7) Potencia''')

opc = int(input('Dame la opción de operación que deseas realizar: '))

if sum <= opc <= pot:
    num1 = int(input('Dame el primer valor: '))
    num2 = int(input('Dame el segundo valor: '))
    if opc == sum:
        print(f'La suma es {num1} + {num2} = {num1+num2}')
    elif opc == res:
        print(f'La resta es {num1} - {num2} = {num1-num2}')
    elif opc == mult:
        if num1 == 0 or num2 == 0:
            print('No puedes ingresar cero en el divisor para esta operación porque siempre será 0')
        else:
            print(f'La multiplicación es {num1} x {num2} = {num1*num2}')
    elif opc == div:
        if num2 == 0:
            print('No puedes ingresar cero en el divisor para esta operación porque es INFINITO')
        else:
            print(f'La divisón es {num1} / {num2} = {num1/num2}')
    elif opc == divEnt:
        if num2 == 0:
            print('No puedes ingresar cero para esta operación porque es INFINITO')
        else:
            print(f'La divisón entera es {num1} // {num2} = {num1//num2}')
    elif opc == mod:
        if num2 == 0:
            print('No puedes ingresar cero para esta operación porque no tendrá RESIDUO')
        else:
            print(f'El módulo es {num1} % {num2} = {num1%num2}')
    elif opc == pot:
        print(f'El número {num1} a la potencia {num2} = {num1**num2}')
else:
    print('No existe esa opción vuelve a intentar')
