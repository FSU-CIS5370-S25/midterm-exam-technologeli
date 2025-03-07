all:
	gcc -fno-stack-protector -z execstack -o stack stack.c
	sudo chown root stack
	sudo chmod 4755 stack

