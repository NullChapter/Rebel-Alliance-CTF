# Steganography 

## Storyline 

## Flag 

NULL{/flag = steg:found:key:M0xA}

## Setup 

**This txt file must not be disclosed to participants. Contains flag and answers**

_What is this ?_
This is steganography challenge for the CTF where the flag is hidden in plain sight within the image. Try different and interesting ways to extract the necessary data that's hidden in the image.

_How is it done?_
1. Have the image and the flag in the same directory. 
2. Use cmd command, "copy /b" to merge the image file and flag text document. 
3. The flag is converted to binary form. 

_How to decode it?_
1. We can inspect the image by opening it with notepad (in windows) 
2. we can use command line to convert the image to a string format and inspect the file. 
3. We can use Python to read the file and inspect it for the flag. 
4. We can use online tools (not recommended)

_Hints_
The flag is hidden in plain sight and just needs some basic inspection.

_details_
Stego File Name: star_wars_stego_image.png (2.22MB) 
Challenge Author: Tharun R 
Github Username: IHac-er

Flag of the challenege = NULL{steg:found:M0xA}