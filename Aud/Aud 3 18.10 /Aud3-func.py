a = []
for i in range(1,10):
    if i % 2 == 0:
         a.append(i)
print(a)

b = [i for i in range(1,10) if i % 2 == 0]
print(b)