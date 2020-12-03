"""
Вводится N чисел в стоблик. Найти пару, чьё произведени максимально
и делится на 80. Вывести эту пару
"""

# TODO add comments

total = int(input())

ostatki = [0] * 80

# предополагаемая пара
a = b = 0

for i in range(total):
	novoe = int(input())

	ostatok_pervoe = novoe % 80
	ostatok_pari = (80 - ostatok_pervoe) % 80

	if novoe * ostatki[ostatok_pari] > a * b:
		a = novoe 
		b = ostatki[ostatok_pari]

	if novoe > ostatki[ostatok_pervoe]:
		ostatki[ostatok_pervoe] = novoe

print(a, b)


