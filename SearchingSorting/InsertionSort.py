def swap(x,y):
    return (y,x)

def insertionSort(array):
    for i in range(1, len(array)): #start from 2nd element in array
        key = array[i]
        j = i-1
        while(j>=0 and array[j]>key):
            array[j+1] = array[j]
            j = j-1
        array[j+1] = key
    return array

if __name__ == '__main__':
    arr = [1, -3, 6, 5, 10, -100]
    print arr
    print insertionSort(arr)