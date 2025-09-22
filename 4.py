def ans():
    maxi = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1): 
            product = i * j
            if product <= maxi:
                break 
            if ispal(str(product)):
                maxi = product
    return maxi