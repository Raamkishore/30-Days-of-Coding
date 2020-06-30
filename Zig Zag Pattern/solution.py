n = list(input())

m = int(input()) + 1

count = 0

for i in range(1, m):

    j = 0

    if i % 2 == 0:
        even = 1
        odd = 0
    else:
        even = 0
        odd = 1

    if odd:

        for j in range(m-i-1):
            print('*', end = '')
            j += 1

        for k in range(j, m-1):
            if count < len(n):
                print(n[count], end = '')
                count += 1
            else:
                print('#', end = '')

    if even:
        
        for j in range(i):
            if count < len(n):
                print(n[count], end = '')
                count += 1
            else:
                print('#', end = '')
            j += 1

        for k in range(j, m-1):
            print('*', end = '')

    print()
