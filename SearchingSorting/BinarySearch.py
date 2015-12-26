#! /usr/bin/python
def binarySearchRecursive(array, low, high, element):
    if (high >= low): #base case
        mid = (low+high)/2
        if (element == array[mid]):
            return mid
        elif (element >= array[mid]):
            return binarySearchRecursive(array, mid+1, high, element)
        else:
            return binarySearchRecursive(array, low, mid-1, element)
    else:
        return -1

def binarySearchIterative(array, low, high, element):
    while (high >= low):
        mid = (low+high)/2
        if (array[mid] == element):
            return mid
        elif(array[mid] < element):
            low = mid+1
        else:
            high = mid-1
    return -1

if __name__=='__main__':
    sorted_arr = [1,3,5,7,9]
    
    '''
    #Use of sorted() function in python to sort an unsorted array
    unsorted_arr = [2,4,8,6.5,10,-2,0]
    unsorted_arr = sorted(unsorted_arr)
    print unsorted_arr
    '''
    
    print binarySearchRecursive(sorted_arr, 0, len(sorted_arr)-1, 5) 
    print binarySearchIterative(sorted_arr, 0, len(sorted_arr)-1, 5)
    