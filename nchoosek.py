#Returns the value of n choose k.

def nchoosek(n,k):
    if (n<0 or k<0):
        pass
    elif (n<k):
        return 0
    else:
        result_1 = 1
        for i in range(0,n-k):
            result_1 *= (n-i)
        result_2 = 1
        for i in range(1,n-k+1):
            result_2 *= i
        return result_1//result_2
    
