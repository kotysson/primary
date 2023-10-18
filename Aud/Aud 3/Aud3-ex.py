matrix = [[1, 2, 3], [4, 5]]
c = []
for i in matrix:
    for a in i:
        c.append(a)
print(c)

one_dim = [j for i in matrix for j in i]
print(one_dim)

# task 2
a = []
for i in range(1, 6):
    e = i * i
    a.append((i, i*i))
print(a)

b = [(i, i * i) for i in range(1, 6)]
print(b)

# task 3
string = "This is a sample sentence"
spisok = string.split(' ')
x = []

for i in spisok:
    if len(i) > 4:
        x.append(i)
print(x)

y = [i for i in spisok if len(i) > 4]
print(y)

