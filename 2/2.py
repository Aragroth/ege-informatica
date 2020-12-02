# Построить таблицу истинности для какого-то выражения
# достаточно раскрыть операцию "следование" в сложение

from itertools import product

data = list(product([0, 1], repeat=4))
f = lambda x, y, z, w: ((not y or x) or (not z and w)) == (w==x)

print(*list("wxyz"), "answ")
for i in data:
	print(i[0], i[1], i[2], i[3], int(f(*i)))

