def squares(a, b):

    aa = True
    bb = True
    initial = 0
    final = -1
    while(aa or bb):
        
        if(aa):
            sqr = math.sqrt(a)
            if math.ceil(sqr) - sqr == 0:
                initial = sqr
                aa = False

        if(bb):
            sqr1 = math.sqrt(b)
            if math.ceil(sqr1) - sqr1 == 0:
                final = sqr1
                bb = False
        
        a += 1
        b -= 1
        

    return int((final-initial) + 1)
