block_size = 16
test_pt = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
if len(test_pt) % block_size :
    test_pt = test_pt.ljust((len(test_pt)//block_size)*block_size + block_size,"\x00")

test_pt = test_pt.encode().hex()
test_ct = "d69638ed3a5a56af3269c1f5c6c6522ecb8029b32a0f14af327fc2b8d7965167dab33ba93e592ee71d7de7dbbfa9275a" 
key = int(test_pt, 16) ^ int(test_ct, 16)
ct = "d69638ed3a5a56af3269c1f5c6c6522ecb8029b32a0f14af327fc2b8d7965167f08439f40b554bcb72468edbbfa9275a"
pt_int = key ^ int(ct, 16)
pt_hex = f"{pt_int:x}"
pt     = bytes.fromhex(pt_hex).decode('ascii')
print(pt)
