# Steganography 

## Storyline 

## Flag 

NULL{steg:found:M0xA}

## Setup 

**This file must not be disclosed to participants (Contains flag and answers). This file contains directions and details of this challenge**

_What is this ?_
1. This is steganography challenge for the CTF where the flag is hidden in plain sight within the image. Try different and interesting ways to extract the flag data that's hidden in the image.

_How is encoding done?_
1. Have the image and the flag in the same directory. 
2. Use cmd command, "copy /b" to merge the image file and flag text document. 
3. The flag is converted to binary form and embedded/added to the end of the image file.
4. The prodiced output image will have the flag encoded into it. Experiment various methods to encode the flag. 

_How to decode it?_
1. We can inspect the image by opening it with notepad (in windows). This will open binary data of the image which can be inspected to find the flag which is embedded.  
2. we can use command line (cmd in windows and terminal in macOS) to view binary data of the image using "strings" command.
3. We can use Python to open the image. Python will interpret the image as binary data and output the binary data of the image (same as notepad). 
4. We can use online tools to extract unsual contents within a image. (This method is not recommended due to ambiguity).

_How to find the flag after inspecting the image?_
1. After extracting the binary data of the image using the above mentioned methods. 
2. Try to find unusual/odd string of characters that seem to be out of place. 
3. In our case, it is string of 0's and 1's. Convert this binary string to normal text, which is the flag. 

_Hints to be given to participants_
1. The flag is hidden in plain sight and just needs some basic inspection.
2. Try to find unsual stuff that you might not see otherwise. 

_Details_
1. Stego File Name: star_wars_stego_image.png (2.22MB) 
2. Challenge Author: Tharun R 
3. Github Username: IHac-er

Flag of the challenege = NULL{steg:found:M0xA}