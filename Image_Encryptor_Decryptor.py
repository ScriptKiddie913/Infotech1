print("-------------------------------------------------------Image Encryptor and Decryptor-------------------------------------------------------")
print()
print("The picture should be in .png format \n")

import time
import sys
import getpass
i=0

while i<1:
   print("Enter E for Encryption and D for Decryption or Q for quit")
   select=input()
   if select in ("D","d","Decryption","decryption"):
         print("You have selected Decryption")
         
         try:
             path = input(r'Enter path of Image : ')
             key = int(input('Enter Key for encryption of Image : '))
             print('The path of file : ', path)
             print('Key for Decryption: ', key)
             crypt= open(path,'rb')
             image = crypt.read()
             crypt.close()
             image = bytearray(image)
 
             for index, values in enumerate(image):
                image[index] = values ^ key
             crypt = open(path,'wb')
             crypt.write(image)
             crypt.close()
             print('Decryption Done')
         except Exception:
             print('Error:', Exception.__name__)

         i=i+1
   elif select in("E","e","Encryption","encryption"):
        print("You have selected Encryption")
       
        try:
            path = input(r'Enter path of Image : ')
            key = int(input('Enter Key for encryption of Image : '))
            print('The path of file : ', path)
            print('Key for encryption : ', key)
            crypt = open(path, 'rb')
            image = crypt.read()
            crypt.close()
            image=bytearray(image)
            for index, values in enumerate(image):
                image[index] = values ^ key

            crypt = open(path, 'wb')
            crypt.write(image)
            crypt.close()
            print('Encryption Done')

        except Exception:
            print('Error:', Exception.__name__)

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


