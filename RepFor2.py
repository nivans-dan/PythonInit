'''
RepFor2.py
    script en Python que muestre una cuenta regresiva usando un ciclo For y
    esperando un segundo entre cada número
'''

import os
import time

for num in range(10, -1, -1):
    os.system('cls')
    print(num)
    time.sleep(1)
else:
    print('                                     Feliz Año Nuevo')
