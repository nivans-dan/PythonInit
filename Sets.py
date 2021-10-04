#La diferencia entre un SET y una LIST es que el SET no tiene índice
#Se utiliza cuando no te interesa acomodar nada dentro de la variable, sólo te interesa el contenido
colors = {'Red', 'Green', 'Blue'}
print(colors)
print('Red' in colors) #Busca si se encuentra lo que indiquemos dentro del Set, TRUE o FALSE

colors.add('Violet') #Se agregará lo que pongamos, pero a diferencia de una lista este se agregará al principio
colors.remove('Red') #Busca y borra lo que indiquemos
colors.clear() #Borra todos los datos dentros del SET