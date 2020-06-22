def permutationEquation(p):

    li = []
    for i in range(1, len(p)+1):
        li.append(p.index(p.index(i)+1)+1)
        
    return li
