# F(n) = n, при n ≤ 3
# при n > 3:
#   F(n) = 2*n + F(n–1), при чётном n;
#   F(n) = n*n + F(n-2), при нечётном n;
# Определите количество натуральных значений n на отрезке [1; 100], при которых F(n) кратно 3.

def f(n):
	if n <= 3:
		return n
	if n % 2 == 0:
		return 2 * n + f(n - 1)
	else:
		return n ** 2 + f(n - 2)


c = 0
for i in range(1, 101):
	if f(i) % 3 == 0:
		c += 1

print(c)


