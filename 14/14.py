# сколько цифр "2" в троичной записи числа 9 ** 20 + 3 ** 60 - 125

num = 9 ** 20 + 3 ** 60 - 125
base = 3

newNum = ''

while num > 0:
    newNum = str(num % base) + newNum
    num //= base

print(newNum.count("2"))


