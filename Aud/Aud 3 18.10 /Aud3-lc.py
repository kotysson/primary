# первое задание
a = []
for i in range(4, 24, 2):
    # задаем иф, потому что нам нужны только четные числа
    if i % 2 == 0:
        a.append(i)
print(a)

b = [element for element in range(4, 24, 2) if element % 2 == 0]
print(b)

# второе задание
c = []
for el in range(1, 6):
    # тут условий нет, поэтому иф не нужен
    c.append(el * el)
print(c)

d = [elem * elem for elem in range(1, 6)]
print(d)

# третье задание
list_three = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_second = []
for eleme in list_three:
    if eleme % 2 != 0:
        list_second.append(eleme)
print(list_second)

aa = [ab for ab in list_three if ab % 2 != 0]
print(aa)

cc = ['WOrds', 'are', 'difFerent']
cd = [ellement.lower() for ellement in cc]
print(cd)

dd = []
for eelement in cc:
    temp = eelement.lower()
    dd.append(temp)
print(dd)
