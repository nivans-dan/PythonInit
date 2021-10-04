x = (1, 2, 3, 4, 5) #La Tuple debe tener más de un dato para que sea así
y = tuple((1, 2, 3)) #Estas son dos formas de declarar una Tuple
w = (1,) #Para que sólo sea un elemento dentro de la Tuple debemos ponerle una coma
print(x[1])

del w #Elimina la variable que le indiquemos

#Ejemplo de para qué podría servir
locations = {
    (35.12312, 39.000): "Tokyo",
    (35.12312, 39.000): "New York"
}