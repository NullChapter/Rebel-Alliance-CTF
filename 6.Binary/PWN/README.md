#Hints
1. Understand the source code
2. Find out the bug
   a. To find out the bug, you may need to know some fundamental knowledge about heap in the c program.
   b. In short, a program has two places to keep the "buffers": stack and heap.
Stack keeps the "buffers" that the size is known before the program start. For example, local variables are used by a function.
Heap keeps the "buffers" that the size can only be decided in runtime. For example, an online shop VIP member username in which the system has no way to know how long is the username before the program start, as well as the length of the dynamic list storing these usernames because a modern system should allow admin to add/remove usernames.
3. Check the protection
   PIE will be disabled
4. Exploit
   Exploit and invoke the shell to get the flag

##
hosting :
run docker-compose up in /PWN/env directory
access the shell using   nc localhost:20006

