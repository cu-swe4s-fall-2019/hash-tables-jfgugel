
def h_ascii(key, N):
    
    s = 0
    for i in range(len(key)):
        s += ord(key[i])
    return s % N
    return None

def h_rolling(key, N):
    return None
