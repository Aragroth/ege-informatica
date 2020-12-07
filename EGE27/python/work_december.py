# Имеется набор данных, состоящий из положительных целых чисел. Необходимо определить
# количество пар элементов (ai, aj) этого набора, в которых 1 ≤ i < j ≤ N,
# сумма элементов нечётна, а произведение делится на 13.

data = open("../data/file_a.txt")
data.readline()

ch_del_13 = nch_del_13 = 0
ch_nedel = nch_nedel = 0

for i in data:
	i = int(i)
	if i % 13 == 0:
		if i % 2 == 0:
			ch_del_13 += 1
		else:
			nch_del_13 += 1
	else:
		if i % 2 == 0:
			ch_nedel += 1
		else:
			nch_nedel += 1

print(ch_del_13 * nch_del_13 + ch_del_13 * nch_nedel + nch_del_13 * ch_nedel)
	
