import numpy as np
import galois

GF256 = galois.GF(2**8, irreducible_poly = 0x11b)

def add(a,b):
    return a + b

def scalar_mult(a,k):
    return a*k

def mult(a,b):
    return a@b

def inv(a):
    return np.linalg.inv(a)

#Beware: @ represents matrix multiplication and * represents scalar multiplication, don't mix the two !!!
