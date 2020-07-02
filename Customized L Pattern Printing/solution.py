mat = [
        [69, 50, 96, 12, 13],
        [65, 66, 11, 94, 56],
        [52, 76, 21, 37, 78],
        [77, 38, 63, 49, 87],
        [56, 87, 23, 90, 10]
      ]

ev = 0
od = 1

for i in range(len(mat)):

    if i % 2 == 0:
        even = 1
        odd = 0
    else:
        even = 0
        odd = 1

    if even:

        for j in range(len(mat)-ev-1, ev-1, -1):
            print(mat[ev][j], end = ' ')

        for k in range(ev+1, len(mat)-ev):
            print(mat[k][ev], end = ' ')

        ev += 1

    elif odd:

        for l in range(od, len(mat)-od):
            print(mat[l][len(mat)-od], end = ' ')

        for m in range(len(mat)-od, od-1, -1):
            print(mat[len(mat)-od][m], end = ' ')

        od += 1

    print()

        
       
