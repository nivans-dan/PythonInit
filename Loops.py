foods = ['apples', 'bread', 'cheese', 'milk', 'bananas']

for food in foods: #Food es una variable que sólo existe dentro del for
    if food == 'cheese':
        print("You have to buy this")
        break
    print(food)

print(" ")

for food in foods: #Food es una variable que sólo existe dentro del for
    if food == 'cheese':
        continue #Dice que continúe cuando lo encuentre, pero no imprimirá ese
    print(food)

print(" ")

for number in range(1, 8):
    print(number)

print(" ")

for letter in "Hello":
    print(letter)

print(" ")

count = 4

while count <= 10:
    print(count)
    count = count + 1