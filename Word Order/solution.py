num = int(input())

from collections import OrderedDict

d = OrderedDict()

for i in range(num):
    inp = input()
    if inp not in d:
        d[inp] = 1
    else:
        d[inp] += 1

print(len(d))

for i, j in d.items():
    print(j, end = " ")
