from collections import namedtuple

Capacitor = namedtuple("Capacitor", ["vol", "cap", "cost"])
Storage = namedtuple("Storage", ["vol", "cap", "cost"])

# По условию объёмы кратны 0.5, делаем их кратными единице
n = 6 * 2

# В объём равный нулю, ничего не поместится
data = Storage([0], [0], [0])

# заполняем список доступных типов конденсаторов
available = []

file = open("data");
total_elems = int(file.readline())

for _ in range(total_elems):
	vol, cap, cost = map(float, file.readline().split())
	vol = int(vol * 2)
	available.append(Capacitor(vol, cap, cost))

max_cost = float(file.readline())

for v in range(1, n + 1):
	condidates = []
	
	# все варианты постановок конденсаторов для заданного объёма
	for elem in available:
		if v - elem.vol >= 0:
			condidates.append(
				[
					data.vol[v - elem.vol] + elem.vol,
					data.cap[v - elem.vol] + elem.cap,
					data.cost[v - elem.vol] + elem.cost,
				]
			)
	# может получиться так, что выгоднее вообще не добавлять коденсаторов
	condidates.append((data.vol[v - 1], data.vol[v - 1], data.cost[v - 1]))
	# максимальный по объёму и минимальный по цене (с максимальной ёмкостью)
	best_value = sorted(condidates, key=lambda x: (x[0], -x[2], x[1]), reverse=True)[0]
	
	data.vol.append(best_value[0])
	data.cap.append(best_value[1])
	data.cost.append(best_value[2])

print(
	"Самая большая ёмкость при заданном значении стоимости и максимальном объёме равна:",
	[cap for cap, cost in zip(data.cap, data.cost) if cost <= max_cost][-1]
)
