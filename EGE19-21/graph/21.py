print("Исх.\tПетя\tВася\tПетя\tВася")

hod_num = 31
total_sum =  83


def print_line(f, s, hod):
    if i == hod_num:
        print('\n' + '\t' * (hod - 1) + str(f), s, end='')

def print_res(val):
    if i == hod_num: print(f" - {val}", end='')

def print_summer(val, hod):
    if i == hod_num:
        print('\n' + '\t' * (hod - 1), val, sep='', end='')


def game(f, s=9, hod=1, n=0):
    print_line(f, s, hod)
    if 1 < hod < 5 and s + f >= total_sum:
        val = (hod - 1) % 2 == 0
        print_res(val)
        return val  # был ли это ход Васи?

    elif hod == 5:
        print_res(s + f >= total_sum)
        return s + f >= total_sum

    elif hod % 2 == 1:
        data = [
            game(f + 1, s, hod + 1, n),
            game(f * 2, s, hod + 1, n),
            game(f, s + 1, hod + 1, n),
            game(f, s * 2, hod + 1, n)
        ]
        print_summer(all(data), hod)
        return all(data)

    data = [
        game(f + 1, s, hod + 1, n),
        game(f * 2, s, hod + 1, n),
        game(f, s + 1, hod + 1, n),
        game(f, s * 2, hod + 1, n)
    ]
    print_summer(any(data), hod)
    return any(data)


for i in range(0, 60):
    game(i)
print()
