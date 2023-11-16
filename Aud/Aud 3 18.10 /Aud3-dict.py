sample_dict = dict()
# словари в фигурных скобках
# кортежи в круглых либо без скобок
# списки в квадратных
sample_dict["animal"] = "dog"
sample_dict["flame"] = "cat"

sample_dict["flame"] = "fire"

print(sample_dict)
print(sample_dict["flame"])

dict1 = {1: "one", 2: "two"}
for key, value in dict1.items():
    print(key, value)

for value in dict1.values():
    print(value)

for key in dict1:
    print(key)

slovar = {"class": "puple", 34.6: 43, ("flame", "fire", "ice", "water"): "nature"}
print(slovar[("flame", "fire", "ice", "water")])
for i, k in slovar.items():
    print(f"{i}: {k}")
