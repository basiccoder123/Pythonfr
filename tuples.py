tuplex = ("hello", True, 3.14, 7)
print(tuplex)

tuplex = (1, 2, 3, 4, 5)
print(tuplex)

tuplex = tuplex + (9,)
print(tuplex)

tuple1 = (50, 10, 50, 20, 50)
count_50 = tuple1.count(50)
print(count_50)

tuplex = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

_slice = tuplex[3:5]
print(_slice)

_slice = tuplex[:6]
print(_slice)

tuplex[0] = 14
print(tuplex)