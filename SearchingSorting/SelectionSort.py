#function to swap two values
from array import array
def swap(x,y):
    return (y,x)

def selectionSort(array):
    
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if (array[j] < array[min_index]):
                min_index = j
        array[i], array[min_index] = swap(array[i], array[min_index])
    return array

if __name__ == '__main__':
    #x = 10
    #y = 20
    array = [1,4,6,-2,0,4.5]
    print array
    array = selectionSort(array)
    print array
    
    