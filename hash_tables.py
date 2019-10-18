import hash_functions
import sys
import time
import random


def reservoir_sampling(new_val, size, V):
    if len(V) < size:
        V.append(new_val)
    else:
        j = random.randint(0, len(V))
        if j < len(V):
            V[j] = new_val


class LinearProbe:
    def __init__(self, N, hash_fucntion):
        self.hash_fucntion = hash_fucntion
        self.N = N

    def add(self, key, value):
        start_hash = self.hash_fucntion(key, self.N)
        pass

    def search(self, key):
        start_hash = self.hash_fucntion(key, self.N)
        pass

class ChainedHash:
    
    def __init__(self, N, hash_method):
        self.hash = hash_method
        self.N = N
        self.T = [ [] for i in range(N) ]
        self.M = 0

    def insert(self, key, value):
        hash_slot = self.hash(key, self.N)
        self.T[hash_slot].append((key,value))
        self.M += 1
        return True

    def find(self, key):
        hash_slot = self.hash(key, self.N)
        for k,v in self.T[hash_slot]:
            if key == k:
                return v
            return None
    
    

