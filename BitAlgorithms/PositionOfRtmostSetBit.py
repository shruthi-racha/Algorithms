from math import log
def getFirstSetBitPos(n):
    return log((n & -n),2) + 1

if __name__ == '__main__':
    print getFirstSetBitPos(12)
