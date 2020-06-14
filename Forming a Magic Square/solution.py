def formingMagicSquare(s):

    total = []
    possible = [
            [8, 1, 6, 3, 5, 7, 4, 9, 2],
            [6, 1, 8, 7, 5, 3, 2, 9, 4],
            [4, 9, 2, 3, 5, 7, 8, 1, 6],
            [2, 9, 4, 7, 5, 3, 6, 1, 8], 
            [8, 3, 4, 1, 5, 9, 6, 7, 2],
            [4, 3, 8, 9, 5, 1, 2, 7, 6], 
            [6, 7, 2, 1, 5, 9, 8, 3, 4], 
            [2, 7, 6, 9, 5, 1, 4, 3, 8]
                ]
    for i in range(len(possible)):
        count = 0
        for j in range(len(s)):
            if s[j] != possible[i][j]:
                count += abs(s[j] - possible[i][j])
        total.append(count)
    
    return min(total)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    c = list(map(int, input().rstrip().split()))

    s = a + b + c

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
