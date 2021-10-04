# Own Modules/Bibliotecas
# Thirdy Party Modules
# Python Modules

import datetime #Libreria/Módulo de Python

print(datetime.date.today()) #Imprime la fecha de hoy
print(datetime.timedelta(minutes=70)) #Transforma los minutos a horas

from datetime import timedelta, date #Aquí especificamos desde antes que 'extensiones' usaremos para acortar el código

print(date.today()) #Imprime la fecha de hoy
print(timedelta(minutes=70)) #Transforma los minutos a horas

from MyModuleMath import add, substract #Módulo que yo creé

add(1, 2)
substract(2, 1)

#PyPi es una página donde podremos descargar módulos de terceros
#Para descargar un módulo sólo escribimos en la consola el nombre de dicho módulo
#Ejemplo: pip instal colorama, y listo se instala solo