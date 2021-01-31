# Python-24-hour-clock
A simple python 24 hour clock to run on my Raspberry Pi3b which will be set to UTC and also run as the lab's time source

# install Python if it isn't already done # https://dev.to/kalebu/how-to-make-a-digital-clock-in-python-4emm
# The source of the Sauce # https://cppsecrets.com/users/218111411511410110199104971141051161049764103109971051084699111109/Python-GUI-Digital-Clock.php
# more Sauce # https://newtechnovice.com/2020/07/05/create-digital-clock-using-tkinter/
# setting UTC # https://realpython.com/python-time-module/


# The commands derived from reading, reading, and more reading - REF are inline as required.
sudo apt-get install python3-tk


# original source code #
import tkinter as tk
import time 
def times():
current_time=time.strftime("%H:%M:%S") 
clock.config(text=current_time)
clock.after(200,times)

root=tk.Tk()
root.geometry("450x250")
clock=tk.Label(root,font=("Arial",50,"bold"),bg="white")

times()

digi=tk.Label(root,text="Digital clock",font="Arial 24 bold")
digi.pack(padx=5, pady=5)
hms=tk.Label(root,text=" hours minutes seconds ",font="Arial 15 bold")
hms.pack(padx=5, pady=5)
clock.pack(padx=5, pady=5)
root.mainloop()


