def swap(x,y):
    return (y,x)

def bubbleSort(array):
    swapped = False
    for i in range(len(array)):
        for j in range(0, len(array)-i-1): #last i elements already in space
            if(array[j] > array[j+1]):
                array[j], array[j+1] = swap(array[j], array[j+1])
                swapped = True
        if (swapped == False):
            break
    return array

if __name__ == '__main__':
    arr = [1, -3, 6, 5, 10, -100]
    print arr
    print bubbleSort(arr)