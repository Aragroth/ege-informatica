"""
Число называется полусовершенным, если сумма всех или некоторых его делителей
(включая единицу и не включая само число), совпадает с этим число. Выведите все
полусовершенные числа из диапазона [300; 350].
"""


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


def is_half_perfect(deliteli, current_sum=0):
	"""Через рекурсию проверяет, является ли число полусовершенным"""
	global num 
	
	# Если сумма равна числу, значит оно полусовершенное
	if current_sum == num:
		return True
	# Если сумма больше числа, то эта комбинация
	# делителей уже точно не подойдёт
	if current_sum > num:
		return False
	# Если больше делителей не осталось, то число не полусовершенно
	# или же эта комбинация делителей не подошла
	if not deliteli:
		return False
	
	# есть два варианта для каждого делителя. Либо мы добавляем его
	# к итоговой "сумме" делителей, либо мы его пропускаем. При этом
	# он в любом случае будет убран из списка делителей.
	return 	is_half_perfect(deliteli[1:], current_sum + deliteli[0]) or \
		  	is_half_perfect(deliteli[1:], current_sum)


for num in range(300, 350 + 1):
	deliteli = factorize(num)
	if is_half_perfect(deliteli):
		print(num)
