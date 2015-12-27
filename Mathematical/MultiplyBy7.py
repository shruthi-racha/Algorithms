'''
Optimized way to multiply a number by 7 is 
to left shift number(n) 3 times -> 8n
subtract n from 8n -> (8n-n) = 7n
'''

def multiplyBy7(number):
   return ((number<<3) - number)
    
if __name__ == '__main__':
    number = 7
    print multiplyBy7(number)
    
#Time Complexity = O(1)
#Space Complexity = O(1)
#Works only for +ve integers
#Same logic can be used to fast multiply by 9 or other numbers