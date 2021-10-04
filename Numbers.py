#10 int
#10.4 float

# print(type(3))
# print(type(3.1)) -> Muestra qué tipo de dato es

# print(2 + 3)

# 1 + 1 #Suma. Dará int = 2
# 1 + 1.0 #Suma. Dará float = 2.0
# 2 - 1 #Resta. Dará int = 1
# 1 * 2 #Multiplicación, Dará int
# 2 ** 3 #Esto es el exponente, dará un total de 8
# 3 / 2 #Dará flotante = 1.5
# 3 // 2 #Devuelve el residuo (módulo) = 1
# 3 % 2 #Es lo mismo que el de arriba (módulo)
# # Respeta el orden en que se resuelven operaciones si juntas varias como 2/2*3%2

age = input("Insert your age: ") #Pide valores y los almacena en una variable
newAge = int(age) + 5 #Se convierte en int(age) porque el valor que da, aunque sea número, siempre será un string/caracter
print(newAge)