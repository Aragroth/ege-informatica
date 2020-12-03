def main(s):
	n = 100
	while s - n >= 100:
		s += 20
		n += 40
	return s

for i in range(0, 500):
	if i != main(i):
		print(i)
