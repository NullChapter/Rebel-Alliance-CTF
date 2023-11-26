#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

#define BUFSIZE 32
#define FLAGSIZE 64

// Modify the flag here
#define FLAG "NULL{binary_JJ}"

void win() {
    // This function is called when the buffer overflow is successfully exploited
    printf("Congratulations! You've triggered the buffer overflow and reached the secret function.\n");
    printf("Flag: %s\n", FLAG);
}

void vuln() {
    char buf[BUFSIZE];

    // Intentionally vulnerable function using fgets
    printf("Please enter your string: ");
    fgets(buf, BUFSIZE, stdin);

    // This print statement should not execute if the buffer overflow is successful
    printf("Okay, time to return... Fingers Crossed... Jumping to 0x%lx\n", (unsigned long)__builtin_return_address(0));
}

int main(int argc, char **argv) {
    // Disable buffering to make input/output more predictable
    setvbuf(stdout, NULL, _IONBF, 0);

    // Drop privileges using setregid
    gid_t gid = getegid();
    setregid(gid, gid);

    vuln();

    return 0;
}

