def oppositeSigns(x,y):
    return ((x^y) < 0)

if __name__ == '__main__':
    print oppositeSigns(5, -10)
    print oppositeSigns(5, 10)