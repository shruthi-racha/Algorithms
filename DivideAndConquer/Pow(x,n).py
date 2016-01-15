def power_helper(x, n):
    temp = 0.0
    if (n == 0):
        return 1
    temp = power(x, n/2)
    if (n%2 == 0):
        return float(temp*temp)
    else:
        return float(temp*temp*x)
        
def power(x,n):
        if (n >= 0):
            return power_helper(x, n)
        else:
            return float(1/power_helper(x, -n))
        
if __name__ == '__main__':
    
    print power(2, 3)
    print power(2.3, 3)
    print power(2, -3)
    print power(2, -3)
    print power(2.3, -3)
    print power(3, 0)
    
#O(log n)