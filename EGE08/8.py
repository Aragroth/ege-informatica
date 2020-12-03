# Петя составляет 5-буквенные слова из букв К, О, Л, У, Н. Каждую букву нужно использовать ровно
# 1 раз, при этом нельзя ставить подряд две гласные или две согласные. Сколько различных кодов
# может составить Петя?

from itertools import product

glasnie = 'ОУ'
soglasnie = 'КЛН'

valid_count = 0

for combination in product(glasnie + soglasnie, repeat=5):
	is_valid = True
	used_letters = []
	for index in range(len(combination) - 1):
		if 	combination[index] in glasnie and \
		  	combination[index + 1] not in glasnie and \
			combination[index] not in used_letters:
			
			used_letters.append(combination[index])
		
		elif 	combination[index] in soglasnie and \
            	combination[index + 1] not in soglasnie and \
				combination[index] not in used_letters:
			used_letters.append(combination[index])
		else:
			is_valid = False
			break	
	
	if is_valid:
		valid_count += 1

print(valid_count)
			
