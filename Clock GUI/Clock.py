import tkinter as tk
import time

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    root.after(1000, update_clock)

root = tk.Tk()
root.title("Clock")

clock_label = tk.Label(root, font=("Helvetica", 48))
clock_label.pack(padx=20, pady=20)

update_clock()

root.mainloop()
