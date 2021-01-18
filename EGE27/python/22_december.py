from dataclasses import dataclass

@dataclass
class Diff:
	ind: int = 0
	val: int = 0
	diff: float = float("+inf")


def recalculate_best_diff(diffs, i):
	global best_diff
	
	for k, v in diffs.items():
		if v % 2 == 1 and v < best_diff.diff:
			best_diff = Diff(ind=i, val=k, diff=v)
		if v % 2 == 1 and v == best_diff.diff and best_diff.val < k:
			best_diff = Diff(ind=i, val=k, diff=v)


f = open("../data/27-B.txt")
n = int(f.readline())
data = [sorted(list(map(int, i.split()))) for i in f]

max_sum_del = max_sum_nedel = 0
best_diff = Diff()
iteration = []

# ищем, которое не делится на 2 нацело
for i in range(n):
	val = max(data[i])
	max_sum_del += val
	iteration.append(val)
	
	diffs = {data[i][ind]: abs(val - data[i][ind]) for ind in range(3)} 
	recalculate_best_diff(diffs, i)

if max_sum_del % 2 == 0:
	max_sum_del += best_diff.val - iteration[best_diff.ind]
	iteration[best_diff.ind] = best_diff.val

for i in range(n):
	del data[i][data[i].index(iteration[i])]


best_diff = Diff()
iteration = []
# ищем, которое делится на 2 нацело
for i in range(n):
	val = max(data[i])
	max_sum_nedel += val
	iteration.append(val)

	diffs = {data[i][ind]: abs(val - data[i][ind]) for ind in range(2)} 
	recalculate_best_diff(diffs, i)
	
if max_sum_nedel % 2 == 1:
	max_sum_nedel += best_diff.val - iteration[best_diff.ind]
	iteration[best_diff.ind] = best_diff.val

for i in range(n):
	del data[i][data[i].index(iteration[i])]

print(sum([v[0] for v in data]))
