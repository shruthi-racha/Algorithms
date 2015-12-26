#!/usr/bin/python
def linearSearch(array, element):

    for i in range(len(array)):
        if (array[i] == element):
            return i
    return -1
    '''
    #another way
    for i in array:
        if (element==i):
            return 1
    return -1
    '''

#Code execution starts here
if __name__ =='__main__':
    arr = [1,3,5,6,4.5]
    '''
    #Using python's inbuilt 'in' operator
    x = 4.5
    y = 5.5
    
    if x in arr:
        print 1
    else:
        print -1
        
    if y in arr:
        print 1
    else:
        print -1
    '''    
    print linearSearch(arr, 4.5)