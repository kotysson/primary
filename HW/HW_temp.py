temp_f = float(input("Введите температуру в градусах по Фаренгейту в формате xx.x: "))
temp_c = (temp_f - 32) / 1.8
temp_c = round(temp_c, 2)
print("Температура в градусах по Цельсию: ", temp_c)
