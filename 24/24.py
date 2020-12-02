data = open("24-5.txt").readline()

vals = [i + 1 for i, x in enumerate(data) if x == '(']
print(vals[10000 - 1])
