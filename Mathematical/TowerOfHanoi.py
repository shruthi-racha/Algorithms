def towerOfHanoi(no_of_disks, source, destination, temp):
    if (no_of_disks == 1):
        print "Move disk 1 from " + str(source) + " to " + str(destination)
        return
    else:
        towerOfHanoi(no_of_disks - 1, source, temp, destination)
        print "Move disk " + str(no_of_disks) + " from " + str(source) + " to " + str(destination)
        towerOfHanoi(no_of_disks - 1, temp, destination, source)
        
if __name__ == '__main__':
    towerOfHanoi(4, 'A', 'C', 'B')
    
#No. of Moves for n disks = 2^n - 1