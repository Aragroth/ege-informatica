def calc(n, cur=0):
	if n == 24:
		return True
	if n > 24:
		return False
	cur += calc(n * 2)
	cur += calc(n + 2)
	
	return cur


print(calc(1))


