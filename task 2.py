
a = [1, 4, 6]
b = [11, 33, 22]
c = [a for _, a in sorted(zip(b, a))]
print(c)