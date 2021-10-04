product = {
    "name": "book",
    "quantity": 3,
    "price": 4.99
}

person = {
    "firstName": "Dan",
    "lastName": "Nava"
}

print(person.keys()) #Nos devolverá sólo el nombre de las llaves (los que están del lado izquierdo antes de ":")
print(person.items()) #Nos devolverá todos los valores dentro del Diccionario
person.clear() #Borra todo el contenido del Diccionario

#Se puede crear una Lista que dentro contenga varios Diccionarios
products = [
    {"name": 'book', "price": 10.99},
    {"name": 'laptop', "price": 150.99}
]