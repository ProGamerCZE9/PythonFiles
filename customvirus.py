import os # Do not change this
import webbrowser # Do not change this
import time # Do not change this
from colorama import Fore, init
init(convert=True) # Do not change this

print(Fore.RED + "WARNING!")
print(Fore.RED + "If you run this program, we do not take responsibility for computer crash.") # Here you can leave warning (recommended)
run = input(Fore.RED + "Do you really wanna run this program? yes/no: ")
if run == "yes":

 while True: 


    os.startfile('cmd') # You can write here any program you have.
    os.startfile('notepad') # You can write here any program you have.
    webbrowser.open('Your Website url') 
    webbrowser.open('Your Website url')
    webbrowser.open('Your Website url')

if run == "no":
  print("")
  print(Fore.RED + "You said", run)
  time.sleep(1.5)
  print("")
  time.sleep(0.1)
  print(Fore.RED + "Press Enter to close the program")
  time.sleep(1)
  input("")
  exit(123)
  input()
else:
    exit(123)
    input()
