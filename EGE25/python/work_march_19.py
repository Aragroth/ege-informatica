import multiprocessing
import math
import time

start = time.time()


def func(r):
    start, end = r[0], r[1]
    data = []
    for number in range(start, end):
        if number % 1000000 == 0:
            print(number)
        count = 0
        mass = set()
        middle = math.floor(math.sqrt(number))

        for delitel in range(1, middle + 3):
            if number % delitel == 0 :
                if delitel ** 2 == number:
                    mass.update({delitel})
                    break 

                if len(mass) > 5:
                    break

                if delitel % 2 == 1:
                    mass.update({delitel})
                if (number // delitel) % 2 == 1:
                    mass.update({number // delitel})

        if len(mass) == 5:
            print('<-------', number)


with multiprocessing.Pool(multiprocessing.cpu_count()) as p:
    ranges = []
    for i in range(40_000_000, 50_000_000, 10_000):
        ranges.append([i, i + 10_000])
    ranges[-1][1] += 1

    p.map(func, ranges)



print(time.time() - start)
