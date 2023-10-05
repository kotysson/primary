mark = 0

while mark not in range(1, 11):
    mark = int(input("Введите оценку от 1 до 10\n"))

if mark in range(1, 3):
    print(f"Ваша оценка: {mark}, неудовлетворительно")
elif mark in range(3, 5):
    print(f"Ваша оценка: {mark}, удовлетворительно")
elif mark in range(5, 8):
    print(f"Ваша оценка: {mark}, хорошо")
else:
    print(f"Ваша оценка: {mark}, отлично")
