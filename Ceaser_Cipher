print("-------------------------------------------- Caesar Cipher Tool --------------------------------------------------")
print("\n")
import time
import sys
import getpass
i=0
crypt=""

while i<1:
   print("Enter E for Encryption and D for Decryption or Q for quit")
   select=input()
   if select in ("D","d","Decryption","decryption"):
         print("You have selected Decryption")
         t=getpass.getpass(prompt="Enter the message (invisible): ")
         i=i+1
   elif select in("E","e","Encryption","encryption"):
         print("You have selected Encryption")
         t=getpass.getpass(prompt="Enter the message(invisible):")
         i=i+1
   elif select in("q","Q","Quit","quit"):
       print("Quitting cipher in")
       print("3")
       time.sleep(1)
       print("2")
       time.sleep(1)
       print("1")
       time.sleep(1)
       sys.exit(0)
   else:
         print("You have entered a wrong choice \n Try Again \n \n")
         time.sleep(3)
letters = sum(c.isalpha() for c in t)
digits = sum(c.isdigit() for c in t)
special = len(t)-letters-digits
print("No. of letters is "+ str(letters))
print("No. of digits is "+str(digits))
print("No. of special characters is "+str(special))
print("Enter the key for the cipher:")
key=getpass.getpass(prompt="Enter the key(invisible):")
le=len(t)
if select in  ("D","d","Decryption","decryption"):         
       for x in range(le):
              if t[x].islower()==True:
                 start=ord("a")
              else:
                 start=ord("A")
              cr=str(chr((ord(t[x])-int(start)-int(key)) % 26 + int(start)))
              crypt=crypt+cr
       print("Decrypted text is: \n " + crypt)
    
if select in ("E","e","Encryption","encryption"):         
     for x in range(le):
            if t[x].islower()==True:
                 start=ord('a')
            else:
                 start=ord('A')
            cr=(chr((ord(t[x])-int(start)+int(key)) % 26+int(start)))
            crypt=crypt+cr
     print("Encrypted text is: \n " + crypt)
     
