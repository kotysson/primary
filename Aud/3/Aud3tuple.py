sample_tuple = (0, "dog", {0: "dog"})
print(type(sample_tuple))

a = len(sample_tuple)
print(a)

print(sample_tuple[1])

# удаление элемента из кортежа напрямую невозможно: он неизменяем
# для модификации можно сделать список из нужных эл-тов кортежа
# и превратить список обратно в кортеж
test_tuple = (30, 31, 40, 50)
test_list = [i for i in test_tuple if i != 31]
print(test_list)
final_tuple = tuple(test_list)
print(final_tuple)
