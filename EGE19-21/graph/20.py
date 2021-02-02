print("Исх.\tПетя\tВася\tПетя")

cur_hod = 31

def game(f, s=18, hod=1):
    if i == cur_hod:
        print('\n' + '\t' * (hod - 1) + str(f), s, end='')
    if hod <= 3 and s + f >= 83:
        if i == cur_hod: print(" - False", end='')
        return False
    if hod > 3:
        if i == cur_hod: print(" -", s + f >= 41, end='')
        return s + f >= 83

    if hod % 2 == 1:
        data =  [game(f+1, s, hod + 1),
                game(f*2, s, hod + 1),
                game(f, s+1, hod + 1),
                game(f, s*2, hod + 1)]
        if i == cur_hod: print('\n' + '\t' * (hod - 1), any(data), sep='', end='') 
        return any(data)
    data  = [game(f+1, s, hod + 1),
            game(f*2, s, hod + 1),
            game(f, s+1, hod + 1),
            game(f, s*2, hod + 1)]
    if i == cur_hod: print('\n' + '\t' * (hod - 1), all(data), sep='', end='')
    return all(data)


for i in range(1, 32):
    game(i)
print()
