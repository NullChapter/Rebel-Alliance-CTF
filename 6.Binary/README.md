# Binary - The Memory Maze

## Storyline 

Amidst the chaos of the Galactic Civil War, a team of rebel hackers embarks on a daring mission to infiltrate an Imperial research facility known for its advanced memory allocation system.
Led by the cunning "Heap Master," the rebels must navigate through a labyrinth of intricate coding and security measures to access vital intelligence crucial to the Rebel Alliance's cause.
With the help of their trusty astromech droid, the rebels exploit a critical flaw in the facility's memory allocation, allowing them to gain control over the Imperial security protocols and access classified information.

Challenge: The Task for the HEAP MASTER is to find the flag by invoking the shell
## Flag 
Null{rions_blr_buff}
## Hints

1. Understand the source code
2. Find out the bug
    a. To find out the bug, you may need to know some fundamental knowledge about heap in the c program.
    b. In short, a program has two places to keep the "buffers": stack and heap. Stack keeps the "buffers" that the size is known before the program start. For example, local variables are used by a function. Heap keeps the "buffers" that the size can only be decided in runtime. For example, an online shop VIP member username in which the system has no way to know how long is the username before the program start, as well as the length of the dynamic list storing these usernames because a modern system should allow admin to add/remove usernames.
3. Check the protection PIE will be disabled
4. Exploit Exploit and invoke the shell to get the flag
 
