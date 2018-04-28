#Computes minimum number of random persons in a group such that
#at least two people share a birthday with probability p.

p = float(input('Enter desired probability. '))
n = 1
p_temp = 1
i = 1

if (p == 1):
    print('N at least 365.')
else:
    while (p_temp > (1.0-p)):
        p_temp = p_temp*(365-i)/365
        n += 1
        i += 1
    print(n)
