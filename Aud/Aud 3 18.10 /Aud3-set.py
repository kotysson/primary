sample_set = {0, 1, 20, 0, "play"}
# множества видят только уникальные значения
# множество не хранит порядковый номер элемента
print(type(sample_set))

list1 = [1, 2, 2, 3, 4, 5, 5]
set1 = set(list1)
print(set1)

test_set = {i for i in range(1, 11)}
print(test_set)

# залочить множество можно с помощью frozenset
# frozenset не позволяет менять множество, поэтому команда ниже не выполнится
test_set = frozenset(test_set)
# вернуть класс множества можно по стандартному методу
test_set = set(test_set)
print(type(test_set))
test_set.add(12)
print(test_set)
