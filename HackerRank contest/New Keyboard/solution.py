S = input()

numbers = [str(i) for i in range(10)]

home, end, num = 0, 1, 1

hom = []
ed = []

ch = ['<', '>', '#']

for i in S:
    if i in ch:
        if i == '<':
            if home:
                if len(hom):
                    ed = hom + ed
                    hom = []
            else:
                home = 1
                end = 0
        elif i == '>':
            home = 0
            end = 1
        elif i == '#':
            if num:
                num = 0
            else:
                num = 1
    else:    
        if home:
            if i == '*':
                if len(hom):
                    hom.pop()
            elif i.isalpha() or i == '_':
                hom.append(i)
            else:
                if num:
                    hom.append(i)

        elif end:
            if len(hom):
                ed = hom + ed
                hom = []
            if i == '*':
                if len(ed):
                    ed.pop()
            elif i.isalpha() or i == '_':
                ed.append(i)
            else:
                if num:
                    ed.append(i)
            
if len(hom):
    ed = hom + ed
            
print(''.join(ed))
