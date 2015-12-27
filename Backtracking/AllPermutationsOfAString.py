def swap(list, start, end):
    temp = list[start]
    list[start] = list[end]
    list[end] = temp
    return list
    

def toList(string):
    temp = []
    for x in string:
        temp.append(x)
    return temp

def toString(list_of_string):
    #print list_of_string
    #print ''.join(list_of_string)
    return ''.join(list_of_string)

def permute(list_of_string, start, end):
    if (start == end):
        print toString(list_of_string)
    else:
        for i in xrange(start, end+1):
            list_of_string = swap(list_of_string, start, i)
            permute(list_of_string, start+1, end)
            list_of_string = swap(list_of_string, start, i)
            
if __name__ == '__main__':
    string = "ABC"
    list_of_string = toList(string)
    start = 0
    end = len(list_of_string)-1
    permute(list_of_string, start, end)