from C_starter import *

global m
m = GF256([[0x02, 0x03, 0x01, 0x04], [0x02, 0x08, 0x13, 0x01], [0x07, 0x01, 0x02, 0x83], [0x13, 0x02, 0x09, 0x02]])
block_size = 16

def bytes2matrix(text):
    #Converts a 16-byte array into a 4x4 matrix.
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    #Converts a 4x4 matrix into a 16-byte array.
    the_text=b""
    for l1 in matrix:
        text= bytes(l1)
        the_text += text
    return the_text

def find_key(block_p, block_c):
    bp = GF256(bytes2matrix(block_p))
    bc = GF256(bytes2matrix(block_c))
    return matrix2bytes(inv(m)@bc - m@bp)

def decrypt(ct,key):
    assert len(ct)%16==0
    pt = b""
    for i in range(len(ct)//16):
        pt += decode(ct[16*i:16*(i+1)], key)
    return pt

def decode(block_c, key):
    k  = GF256(bytes2matrix(key))
    bc = GF256(bytes2matrix(block_c))
    return matrix2bytes(inv(m)@inv(m)@bc - inv(m)@k)

test_pt = b"https://www.youtube.com/watch?v=dQw4w9WgXcQ"
test_ct = "06b8f07148a81ada030eff102320494dc18674d3db2e2fdc1d2c62858485d2c0207c616c670e79c88ae5f13fb758b098" 
test_ct = bytes.fromhex(test_ct)

if len(test_pt) % block_size :
    test_pt = test_pt.ljust((len(test_pt)//block_size)*block_size + block_size,b"\x00")

block_pt = test_pt[0:16] #Taking just one block to find the key.
block_ct = test_ct[0:16]
key = find_key(block_pt, block_ct)
print(int.from_bytes(key, byteorder='big'))

ct = "06b8f07148a81ada030eff102320494dc18674d3db2e2fdc1d2c62858485d2c0a71993b6034da49f3f38ad9a63f6f49d"
ct = bytes.fromhex(ct);
pt_bytes = decrypt(ct, key)
pt     = pt_bytes.decode('ascii')
print(pt)
