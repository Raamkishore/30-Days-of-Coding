def minimumLoss(price):

    count = sys.maxsize
    temp = sorted(price)

    for i in range(1, len(temp)):
        if temp[i] - temp[i-1] < count:
            if price.index(temp[i]) < price.index(temp[i-1]):
                count = temp[i] - temp[i-1]

    return count
