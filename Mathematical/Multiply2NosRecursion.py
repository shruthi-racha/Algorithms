def multiptly(first,second):
    if(second == 0):
        return 0
    elif(second > 0):
        return (first+multiptly(first, second-1))
    else: #y is negative
        return -1*multiptly(first, -second)
    
if __name__=='__main__':
    #print multiptly(5, 6)
    print multiptly(4, -7)
    