# Forensics 
Macro-enabled PowerPoint files (PPTM) are often used to distribute malicious content because macros can be used to execute arbitrary code on a user's system when the file is opened. This makes them a common vector for malware distribution in phishing attacks and other forms of cyberattacks.
## Storyline 

## Flag 
NULL{F043&SIX}
## Setup 
Put the pptm file in a drive or github and share the link 
## investigation steps
-> mostly people will look into the malicious scripts in the macro enabled ppt's 
-> in our ctf there won't be any scripts ....
-> simply extracting the .pptm files solves the problem extract using binwalk -e "name_of_the_file"
-> after extracting the zip contains n number of file 
-> how you'll search using grep ? yes but here's the one line command that retrieves the information quicker "find -D tree|grep flag "
-> the flag contains the hint to next folder where the flag is encoded 
-> after decoding you'll get the flag 
