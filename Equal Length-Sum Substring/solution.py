def res():

    n = input()

    j = len(n) // 2
    boo = False

    if len(n) <= 1:
        print('-1')
    else:
        boo = True
  
    while boo:
        
        i = 0
        temp = j
        boo1 = True

        while boo1:

            if temp+j <= len(n):

                f = [int(k) for k in n[i:temp]]
                l = [int(k) for k in n[temp:temp+j]]

                if sum(f) == sum(l):

                    return ''.join(n[i:temp]) + ''.join(n[temp:temp+j])

                    boo = False
                    boo1 = False
                    
                else:

                    i += 1
                    temp += 1

            else:

                boo1 = False

        j -= 1

        if j == 0:
            boo = False
            return -1

print(res())
