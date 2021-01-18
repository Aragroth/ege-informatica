from typing import List, Union

file = open("../data/26.txt")
total_vals, max_size = map(int, file.readline().split())

values = sorted([int(i) for i in file])

big_cargos = [i for i in values if 210 <= i <= 220]

data = [None for _ in range(sum(big_cargos))]
data.append(big_cargos)

for mass in range(sum(big_cargos) + 1, max_size + 1):
    if mass % 1000 == 0:
            print(mass)

    condidates = []
    for cargo in values:
        previous = mass - cargo
        if previous >= 0 and data[previous] is not None and data[previous].count(
                cargo) < values.count(cargo):
            condidates.append(data[previous] + [cargo])

    condidates.append(data[mass - 1])

    best_cargo = sorted(condidates, key=lambda x: (len(x), sum(x)), reverse=True)[0]
    data.append(best_cargo)

print(sum(data[-1]), len(data[-1]))

