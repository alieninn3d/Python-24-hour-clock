# Time Server visual display reading time in 
# Universal Coordintated Time (UTC)
# so the electronics LAB nerd can see the time
#

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
