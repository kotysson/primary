x = int(input())

if x > 20:
    print("x more than 20")
elif x > 10:
    print("x more than 10, but less than 20")
else:
    print("x less or even to 10")


a = int(input())

if a > 0:
    print("a is a positive number")
elif a < 0:
    print("a is a negative number")
else:
    print("a is even to zero")


side1, side2, side3 = 10, 15, 14
if side1 == side2 == side3:
    print("равностор.")
elif (side1 == side2) or (side2 == side3) or (side1 == side3):
    print("равнобедр.")
else:
    print("разностор.")

# проверка длины списка - len
text = str(input())

if len(text) == 0:
    print("Empty string")
else:
    print(f"text len = {len(text)}")

age = int(input("Сколько вам полных лет?\n"))
if age >= 18:
    print("Вы можете голосовать!")
else:
    print("Вы не можете голосовать!")
