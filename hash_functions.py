
def h_ascii(key, N):
    
    s = 0
    for i in range(len(key)):
        s += ord(key[i])
    return s % N
   


def h_polynomial_rolling(key, N, p=53, m=2**64):

    s = 0
    for i in range(len(key)):
        s += ord(key[i]) * p**i
    s = s % m
    return s % N 


 

