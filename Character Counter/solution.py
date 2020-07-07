n = int(input())

n = str(n)

temp = '9'
res = 0

for i in range(len(n)-1):
    res += int(temp) * (i+1)
    temp += '0'

res += ((int(n) - int('9'*(len(n)-1))) * len(n))

print(res)

