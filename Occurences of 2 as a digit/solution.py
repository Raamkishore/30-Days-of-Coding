def numberOf2sinRange(n):
    count = 0
    
    for i in range(n+1):
        i = list(str(i))
        count += i.count('2')
        
    return count

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        print(numberOf2sinRange(n))
