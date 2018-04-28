# Computes the probability of getting n heads (or tails) in m coin flips.

def coins_flips(n,m):
    if (n>m):
        pass
    else:
        result_1 = 1
        for i in range(0,n-k):
            result_1 *= (n-i)
        result_2 = 1
        for i in range(1,n-k+1):
            result_2 *= i
        combins = result_1/result_2
        p = combins*0.5**n
        return p
        
