"""
Для уменьшения аварий на центральной дороге в городе X дорожная служба решила
выровнять ямы. Новая яма будет иметь второй по величине объем (в литрах) среди
её самой и двух соседних ям. При этом размеры первой и последней ямы решили
не менять.

Ночью перед ремонтом дороги в городе X прошел проливной дождь, поэтому все
ямы до краев заполнены водой. Сколько литров воды выльется обратно на дорогу
после проведения ремонта?
Пример входного файла:
8
10
12
8
6
20
12
16
10

При таких исходных данных после ремонта объем ям будет выглядеть следующим
образом 10, 10, 8, 8, 12, 12, 12, 10. В ответе необходимо указать два
числа – 2 и 14.
"""
# считываем файл чисел и делаем копию
with open("../data/26-J5.txt") as f:
	_ = f.readline()
	data = [int(x) for x in f]
	vals = data[:]

# последовательно высчитываем второе по величине значения и заменяем
for ind in range(len(data) - 2):
	vals[ind + 1] = sorted([vals[ind], data[ind + 1], data[ind + 2]])[1]

# количество наименьших значений
print(vals.count(min(vals)))

# сумма разностей, без учёта отрицательных разностей
print(sum(a - b for a, b in zip(data, vals) if a - b > 0))

