#!/usr/bin/python

#Naive Solution sum of digits mul of 3 then number is mul of 3
'''
Optimized Solution
------------------
If the diff between set bits in the odd and even
positions in the binary representation of the 
number is divisible by 3 then the number is
a multiple of 3
'''
def convertDecimalToBinaryn(number):
    binary_rep = []
    while(number != 0):
        binary_rep.append(number%2)
        number = number/2
    binary_rep = list(reversed(binary_rep))
    return binary_rep
    
def isMultipleOf3(number):
    if(number < 0): #convert negative number to its positive
        number = number*-1
    
    if (number == 0):
        return True
    elif (number == 1):
        return False
    else:
        binary_rep = convertDecimalToBinaryn(number) 
        i = len(binary_rep)-1
        even_count = 0
        odd_count = 0
        
        while (i>=0):
            if (i%2 == 0 and binary_rep[i] == 1): #if even bit set 
                even_count += 1
            elif (i%2 != 0 and binary_rep[i] == 1): #if odd bit set
                odd_count += 1
            i = i-1
        if ((even_count - odd_count)%3 == 0):
            return True
        else:
            return False
    
if __name__ == '__main__':
    mul_3 = 6
    not_mul_3 = 10
    print isMultipleOf3(mul_3)
    print isMultipleOf3(not_mul_3)
    
#Time Complexity is O(logn)