from collections import namedtuple

Capacitor = namedtuple("Capacitor", ["vol", "cap", "cost"])
Storage = namedtuple("Storage", ["cap", "cost"])

# Всего у нас сколько позиций ёмкости конденсатора. Поскольку по условию
# Они кратны 0.5, мы просто умножаем объём данных на два.
n = 6 * 2 

# Храним данные о стоимостях и ёмкостях для каждого из объёмов
# В нулевую стоимость и ёмкость ничего не поместится, значит там ноль
# Также это позволяет "индексировать" массив объёмами, которые нумеруется с единицы
data = Storage([0] + [None] * n, [0] + [0] * n)

# будем хранить здесь список всех типов конденсаторов
available = []

file = open("data");
total_elems = int(file.readline())

for _ in range(total_elems):
	vol, cap, cost = map(float, file.readline().split())
	vol = int(vol * 2)
	available.append(Capacitor(vol, cap, cost))

max_cost = float(file.readline())

# вычисляем оптимальные значения для каждого из объёмов
for v in range(1, n + 1):
	for elem in available:
		# проверяем, что коденсатор можно поставить (ему хватает объёма)
		if v - elem.vol >= 0:
			# Если это первый конденсатор и мы ничего ещё не просчитывали
			if data.cap[v] is None:
				# Проверяем, выгодно ли добавить этот конденсатор к прошлому значению ёмкости: V[тек.] - V[конд.]
				if data.cap[v - elem.vol] + elem.cap > data.cap[v - 1]:
					data.cap[v] = data.cap[v - elem.vol] + elem.cap
					data.cost[v] = data.cost[v - elem.vol] + elem.cost
				# Или выгоднее ничего не менять и взять значения из предудщего объёма
				else:
					data.cap[v] = data.cap[v - 1]
					data.cost[v] = data.cost[v - 1]
					
			# Если мы пытаемся подставить уже другой конденсатор из набора (отличный от первого)
			else:
				# Проверяем, выгоднее ли этот конденсатор добавить к прошлому значению ёмкости: V[тек.] - V[конд.]
				if data.cap[v] <= data.cap[v - elem.vol] + elem.cap:
					data.cap[v] = data.cap[v - elem.vol] + elem.cap
					data.cost[v] = data.cost[v - elem.vol] + elem.cost
				
				# Возможно, можно заменить конденсатор так, что общая ёмкость не изменится (Она не может стать больше,
				# потому что это проверяется первым условием), а при этом общая стоимость снизится:
				elif data.cost[v] > data.cost[v - elem.vol] + elem.cost and \
				 		data.cap[v] == data.cap[v - elem.vol] + elem.cap:
					data.cap[v] = data.cap[v - elem.vol] + elem.cap
					data.cost[v] = data.cost[v - elem.vol] + elem.cost
	
				# Дальше можно вообще ничего не проверять потому что 'предыдущее' значение объёма
				# мы бы взяли на этапе, когда там None  => текущий конденсатор - это самый выгодный 
		
		elif data.cap[v] is None:
			# Если места не хватает для того чтобы поставить конденсатор, то берём значения из
			# предпоследнего объёма, ведь он самый выгодный, но только если там None
			# (Иначе, там уже есть какой-то более выгодный конденсатор и не трогаем ничего)
			data.cap[v] = data.cap[v - 1]
			data.cost[v] = data.cost[v - 1]

print(data.cap)
print(data.cost)
print(
	"Самая большая ёмкость при заданной стоимости равна:",
	[cap for cap, cost in zip(data.cap, data.cost) if cost <= max_cost][-1]
)


