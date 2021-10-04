myStr = "Hello World"

# print(dir(myStr)) #Al imprimir esto nos mostrará todas las opciones con las que podemos modificar el texto, por ejemplo mostró upper, lo que se hace a continuación

print(myStr.upper()) #Hace que el String se convierta todo en mayúscula
print(myStr.lower()) #Hace que el String se convierta todo en minúscula
print(myStr.swapcase()) #Pone las primeras letras de cada palabra en minúscula y las demás en mayúscula
print(myStr.capitalize()) #Pone en mayúscula sólo la primer letra de la primer palabra, las demás las pone en minúscula
print(myStr.replace('Hello', 'Bye')) #Remplaza el texto que le indico por uno en específico
print(myStr.replace('Hello', 'Bye').upper()) #Se pueden juntar varios métodos (métodos encadenados)
print(myStr.count('l')) #Nos muestra las veces que se repote algo (se puede usar espacio)
print(myStr.startswith('Hello')) #Nos devuelve un TRUE o FALSE dependiendo si encuentra dicha palabra o no, funciona por caracteres
print(myStr.endswith('World')) #Como la opción de arriba, muestra si lo del final se encuentra o no, funciona por caracteres
print(myStr.split()) #Separa a partir de un caracter en blanco, en este caso sería en dos partes
print(myStr.split(',')) #Funciona igual que el de arriba, pero se especifica que se separe a partir de una coma
print(myStr.find('o')) #Devuelve el valor de dónde se encuentra (posición) dicho valor, en este caso sería 4 por Hell'o', contando desde cero
print(len(myStr)) #Muestra la longitud de la variable, iniciando desde cero
print(myStr.index('o')) #Muestra la posición del caracter en la variable, es como .find()
print(myStr.isnumeric()) #Checa si es numérico, dependindo el caso devuleve TRUE o FALSE
print(myStr.isalpha()) #Checa si es alfanumérico, dependindo el caso devuleve TRUE o FALSE
print(myStr[0]) #Imprimirá sólo la posición que se le dé
print(myStr[-1]) #Imprimirá el último valor que se encuentre en la variable (de atrás hacia adelante)

myStr2 = "Nivans"

print("My name is " + myStr2) #Concatena el texto con la variable
print(f"My name is {myStr2}") #Pone la variable dentro del texto con la ayuda de la letra 'f' al principio
print("My name is {0}".format(myStr2)) #Sirve básicamente igual que la forma de arriba, llama a la variable