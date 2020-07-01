from itertools import product

n, m = input().split()
n, m = int(n), int(m)

li = []

for i in range(n):
    li.append(list(map(int, input().split()))[1:])

combi = list(product(*li))

res = list(map(lambda x : sum([i ** 2 for i in x]) % m, combi))

print(max(res))
