# Buffer-Overflow 
Welcome to the Buffer Overflow challenge! This challenge is designed to test your skills in binary exploitation and vulnerability discovery.
Challenge Description

The challenge binary, buffer_overflow_challenge, is a vulnerable program susceptible to buffer overflow attacks. The goal is to exploit this vulnerability to reach the hidden function and retrieve the flag.
Instructions

    Clone the Repository:

    git clone https://github.com/jjahin/buffer_overflow_challenge

    Build the Docker Image '''bash docker build -t buffer_overflow_challenge .

    Run the Docker Container '''bash docker run -p 8888:1234 buffer_overflow_challenge or docker run -it --rm -p 1234:1234 buffer_overflow_challenge

    Access the challenge through the command line

Hints Hint 1: Understanding the Binary Analyze the provided binary to understand its behavior and identify potential vulnerabilities.

Hint 2: Buffer Overflow Basics Learn about buffer overflow attacks and understand how they can be exploited to manipulate program execution.

Hint 3: Function to Reach Identify the hidden function (win()) that you need to reach in order to retrieve the flag.

Hint 4: Input Validation Explore the input validation mechanisms in the program and think about how they might be bypassed.

Hint 5: Memory Layout Investigate the memory layout of the program to understand how the stack is organized during execution.

Flag Format The flag for this challenge is in the format: NULL{********}

//after inputing the string use the binary and attach it in the debugger

Happy hacking!
## Storyline 

You find yourself on a remote space station with a terminal that has a direct connection to the Death Star's communication network. The station is heavily guarded, and you need to navigate through various security measures to reach the terminal.

Upon accessing the terminal, you discover an interface that mimics the iconic Star Wars holographic displays. The ForceLink protocol is represented by a series of interconnected nodes, guarded by digital stormtroopers. Your goal is to carefully craft a malicious payload to exploit a buffer overflow vulnerability in one of the nodes and bypass the stormtrooper defenses.


## Flag 
NULL{Binary_JJ}

## Setup 

Install Docker in your VM
Run the Docker Container '''bash docker run -p 8888:1234 buffer_overflow_challenge or docker run -it --rm -p 1234:1234 buffer_overflow_challenge
