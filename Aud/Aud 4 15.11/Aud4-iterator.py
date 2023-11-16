# lambda-function
# square = lambda x: x**2
# print(square(5))

# iterator
mylist = [0, 1, 2]
# create iterator with key word iter
iterlist = iter(mylist)
# next вызывает след элемент итерируемого объекта. повторение этой операции выводит след/ элементы последовательно
print(next(iterlist))
print(next(iterlist))
print(next(iterlist))

def for_loop(iterable, body_func):
    # body_func - это любая операция, которую мы будем проводить в цикле, напр., лемматизация
    # превращаем условный список в iterable в итерируемый объект
    iterator = iter(iterable)
    while True:
        current_element = next(iterator)
        body_func(current_element)

def func(i):
    print(i ** 2)

for_loop([0, 1, 2, 3, 4, 5], func)