get = lambda f, s, hod: [
    game(f + 1, s, hod),
    game(f * 2, s, hod),
    game(f, s + 1, hod),
    game(f, s * 2, hod),
]


def game(f, s=7, hod=1):
    if (hod - 1) < 3 and f + s >= 77:
        return False
    if (hod - 1) == 3:
        return f + s >= 77

    if hod % 2 == 1:
        return any(get(f, s, hod + 1))
    
    return all(get(f, s, hod + 1))

for i in range(1, 69 + 1):
    if game(i):
        print(i)
