##n = int(input())
##
##n = str(n)
##
##temp = '9'
##res = 0
##
##for i in range(len(n)-1):
##    res += int(temp) * (i+1)
##    temp += '0'
##
##res += ((int(n) - int('9'*(len(n)-1))) * len(n))
##
##print(res)
##
##
    
d = {'a':1, 'b':2,'c':3}

for k, v in d.items():
    print(k, v)
