import os
import subprocess
import tkinter as tk
from tkinter import *
import random
import webbrowser
import sys
import time

# Version 1.0- Initial commit
# Version 1.1- Fixed time bug
# Version 1.2- Fixing more time bug stuff and adding 
# Version 1.3- Fixing performance bug
# Version 1.4- Deleted time and date function for performance 
# Version 1.5- Had to update the Cox communications link

buttonFont = ("Verdana", "25")
welcomeFont = ("Times", "30")
textFont = ("Helvetica", "20")
smallFont = ("Helevica", "15")
version = 1.5
root = tk.Tk()
rad = tk.IntVar()

def runCommand():
    command = rad.get()
    if command == 0:
        webbrowser.open('https://www.youtube.com/')
    elif command == 1:
        subprocess.Popen([r'C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\devenv.exe'])
    elif command == 2:
        subprocess.Popen([r'D:\Steam\Steam.exe'])
    elif command == 3:
        webbrowser.open('https://www.cox.com/residential/home.html')
    elif command == 4:
        subprocess.Popen([r'C:\Users\mbret\AppData\Roaming\Spotify\Spotify.exe'])
    elif command == 5:
        subprocess.Popen([r'C:\Windows\System32\calc.exe'])
    else:
        webbrowser.open('https://www.rentcafe.com/residentservices/sunstone-at-fox-ridge/userlogin.aspx')

def main():
    frame = tk.Frame(root)
    frame.pack()
    root.geometry("780x700") # width and height
    root.configure(background = "gray25")
    root.title("Director")

    bg_d = "gray25" # going for background default
    labelWelcome = tk.Label(root, text = "Welcome to your director!", font = welcomeFont).pack()
    labelChoice = tk.Label(root, text = "What do you need me to do?", font = textFont).place(x = 210, y = 80)
    labelVersion = tk.Label(root, text = "Version: {ver}".format(ver = version), font = smallFont).place(x = 370, y = 660)
    rad_button_YOUTUBE = tk.Radiobutton(root, text = "Open YouTube", value = 0, variable = rad, font = buttonFont, bg = bg_d).place(x = 300, y = 150)
    rad_button_VisualStud = tk.Radiobutton(root, text = "Open Visual Studio", variable = rad, value = 1, font = buttonFont, bg = bg_d).place(x = 300, y = 210)
    rad_button_STEAM = tk.Radiobutton(root, text = "Open Steam", variable = rad, value = 2, font = buttonFont, bg = bg_d).place(x = 300, y = 270)
    rad_button_COX = tk.Radiobutton(root, text = "Open Cox", variable = rad, value = 3, font = buttonFont, bg = bg_d).place(x = 300, y = 330)
    rad_button_SPOTIFY = tk.Radiobutton(root, text = "Open Spotify", variable = rad, value = 4, font = buttonFont, bg = bg_d).place(x = 300, y = 390)
    rad_button_CALC = tk.Radiobutton(root, text = "Open Calculator", variable = rad, value = 5, font = buttonFont, bg = bg_d).place(x = 300, y = 450)
    rad_button_RENT = tk.Radiobutton(root, text = "Pay Rent", variable = rad, value = 6, font = buttonFont, bg = bg_d).place(x = 300, y = 510)
    btnGO = tk.Button(root, text = "GO!", command = runCommand, font = buttonFont, bg = "white").place(x = 240, y = 580)
    btnEXIT = tk.Button(root, text = "Exit", command = root.destroy, font = buttonFont, bg = "white").place(x = 360, y = 580)
    time.sleep(1)

    root.update()
    root.mainloop()

root.update()
main()
