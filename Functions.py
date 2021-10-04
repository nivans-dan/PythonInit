def hello(name = "Person"): #Se le da un valor por defecto por si en la función no se le manda nada para evitar problemas
    print("Hello", name)

hello("Dan")
hello("Billie")
hello("Marie")
hello()

def add(n1, n2):
    return n1 + n2

print(add(10, 30))
print(add(100, 300))

add2 = lambda n1, n2: n1 + n2 #Es otra forma de declarar una función que tenga un return preestablecido

print(add2(10, 3))