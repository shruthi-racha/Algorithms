def decToBinary(number):
    if(number > 1):
        decToBinary(number/2)
    print number%2
        
if __name__ == '__main__':
    print decToBinary(9)