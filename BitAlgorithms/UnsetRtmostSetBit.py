'''
If n is the number than n-1 will pull the 1
from rtmost import set bit to subtract the 1 from.
Hence n&n-1 will unset the rtmost set bit in not
'''

if __name__=='__main__':
    number = 12
    print "Number is: " + str(number) 
    print "Number in Binary is: " + str(bin(number)[2:])
    num_minus_1 = number - 1
    print "Number minus 1 in binary is: " + str(bin(num_minus_1)[2:])
    print "Number after unsetting the rtmost set bit is: "
    print bin(number & num_minus_1)[2:]