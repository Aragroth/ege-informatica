# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку
# [286564; 287270], числа, имеющие максимальное количество различных делителей. Если таких
# чисел несколько, то найдите максимальное из них. В ответе запишите два числа: количество
# делителей найденного числа и его наибольший делитель, не равный самому числу.


def factorize(n):
	"""
	Находит все уникальные делители числа.
	Включая единицу и не включая само число
	"""
	factor = []
	for delitel in range(1, n):
		if n % delitel == 0:
			factor.append(delitel)

	return factor

max_len = 0
num = 0
for i in range(286564, 287270):
	data = factorize(i)
	if len(data) >= max_len:
		max_len = len(data)
		data.sort()
		num = data[-1]

print(max_len, num)
