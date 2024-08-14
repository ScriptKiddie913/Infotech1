import time
print("-------------------------------------------- Password Strength Checker Tool ------------------------------------------------")
print("This tool is meant to check complexity of a password keeping in regard the various password cracking algorithms ")
print("----------------------------------------------------------------------------------------------------------------------------")
print("\n")

import sys
import getpass
print("Take time to read the instructions")
time.sleep(1)
print("This tool is meant to check complexity of a password keeping inregard the various password cracking algorithms")
time.sleep(2)
print("The password should contain:")
time.sleep(1)
print("1.More than 16 characters")
time.sleep(1)
print("2.Small and capital letters, numbers and special characters")

t=getpass.getpass(prompt="Enter the password(invisible): ")
l = sum(c.isalpha() for c in t)
d = sum(c.isdigit() for c in t)
s = len(t)-l-d
print("No. of letters is "+ str(l))
print("No. of digits is "+str(d))
print("No. of special characters is "+str(s))
if len(t)>16:

  if l!=0 and d!=0 and s!=0:
        if d>len(t)/3 and s>len(t)/3:
           print("Insane password")
        if d>len(t)/3 and s<len(t)/3:
           print("Hard password")
        if d<len(t)/3 and s>len(t)/3:
           print("Hard password")
        if d<len(t)/3 and s<len(t)/3:
           print("Password is moderate")
       
else:
    print("Please read the requirements for the password and enter a stronger password")
