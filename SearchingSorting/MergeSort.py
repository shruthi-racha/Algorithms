from heapq import merge

'''
def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        # change the direction of this comparison to change the direction of the sort
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
 
    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    return result
'''

def mergeSort(array):
    if (len(array) <= 1):
        return array
    mid = len(array)/2
    left_half = array[:mid]
    right_half = array[mid:]
    left_half = mergeSort(left_half)
    right_half = mergeSort(right_half)
    return list(merge(left_half,right_half))

if __name__ == '__main__':

    arr = [1, -3, 6, 5, 10, -100]
    print arr
    print mergeSort(arr)
    