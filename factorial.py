#Returns the factorial of an integer n.

def factorial(n):
    if (n<0):
        pass
    else:
        result = 1
        for i in range(1,n+1):
            result *= i
        return result
