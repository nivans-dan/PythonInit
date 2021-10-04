# Formas de hacer una lista
demoList = [1, 'Hello', 3.1, True, [1, 2, 3]]
Colors = ['Red', 'Blue', 'Green', 'Red']
print(Colors)
numbersList = list((1, 2, 3, 4)) #Se necesita una tuple para poder crear la lista así
print(numbersList)

r = list(range(1, 11)) #Le damos un rango de números que llene la lista, pero llega hasta uno antes del segundo parámetro que está entre los paréntesis
print(r)

print(len(Colors)) #Mostrará la longitud de la lista. Para Colors sería de 3
print(Colors[1])
print('Green' in Colors) #Checa si existe lo que le decimos dentro de la lista, devuelve TRUE o FALSE

Colors[1] = 'Yellow' #Sustituye o agrega el valor en el espacio que se indica
print(Colors)

# Métodos dir()
Colors.append('Violet') #Agrega valores a la lista, pasándolos al final. Sólo toma UN valor
Colors.extend(['Black', 'White']) #Para que tome más valores se usa EXTEND y se debe poner entre llaves como una lista
Colors.insert(1, 'Pink') #Inserta valores justo donde le indicas
Colors.insert(len(Colors), 'Gold') #Esto hace que lo mande hasta el final
Colors.pop() #Quita el último valor de una lista, se puede poner las veces que quieras seguidas
Colors.pop(1) #Quita el valor justo donde se le especifica
Colors.remove('Green') #Quita lo que le digamos dentro del paréntesis
Colors.sort() #Ordena alfabéticamente
Colors.sort(reverse=True) #Ordena alfabéticamente, pero al revés
print(Colors.index('Red')) #Devuelve la ubicación de lo que le pidamos
print(Colors.count('Red')) #Devuelve el cuántas veces se repite un valor dentro de una lista
Colors.clear() #Vacía la lista entera