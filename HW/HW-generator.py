# импортируем библиотеку
import random
target_number = random.randint(1, 100)
# задаем счетчик начиная с 1, потому что при 0 счетчик не считает первую попытку
counter = 1

attempt_number = int(input("Сыграем в \"Угадай число\"? Введите целое число от 1 до 100 \n"))
while attempt_number != target_number:
    if attempt_number > target_number:
        attempt_number = int(input("Вы не угадали, загаданное число меньше. Попробуйте еще раз.\n"))
    else:
        attempt_number = int(input("Вы не угадали, загаданное число больше. Попробуйте еще раз.\n"))
    counter += 1

print(f"Поздравляем, вы угадали с {counter}-й попытки!")

