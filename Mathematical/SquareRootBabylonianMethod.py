def findSquareRoot(number):
    x = float(number)
    y = 1.0
    e = 0.00001
    while((x-y) > e): #to avoid infinite loop in case of non-perfect squares
        x = (x+y)/2
        y = number/x
    return round(x,3)

if __name__ == '__main__':
    print findSquareRoot(5)
    print findSquareRoot(4)