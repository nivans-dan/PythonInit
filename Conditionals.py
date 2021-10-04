color = 'Red'

if color  == 'Blue ':
    print("The color is BLUE")
elif color == 'Red':
    print("The color is RED")
else:
    print("Any color")


name = "Dan"
lastName = "Nava"

if name == "Dan":
    if lastName == "Nava":
        print("You're Dan Nava")
    else:
        print("You're not Dan Nava")
else:
    print("You're not Dan")


x = 5
y = 5

if x > 2 and x <= 10:
    print("x is greater than 2 and less than or equal to 10")
if x > 2 or x <= 20:
    print("x is greater than 2 or less or equal than 20")
if (not(x == y)): #Es como != de C
    print("x is not equal y")