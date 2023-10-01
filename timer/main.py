import time
from tkinter import *
from tkinter import messagebox

# creating Tk window
root = Tk()


root.geometry("300x250")


root.title("Time Counter")

# Declaration of variables
hour = StringVar()
minute = StringVar()
second = StringVar()

# setting the default value as 0
hour.set(" 00")
minute.set(" 00")
second.set(" 00")

# Labels for hours, minutes, and seconds
hour_label = Label(root, text="Hours", font=("Arial", 12))
hour_label.place(x=87, y=55)
minute_label = Label(root, text="Minutes", font=("Arial", 12))
minute_label.place(x=141, y=55)
second_label = Label(root, text="Seconds", font=("Arial", 12))
second_label.place(x=200, y=55)

# Use of Entry class to take input from the user
hourEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=hour)
hourEntry.place(x=83, y=20)

minuteEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=minute)
minuteEntry.place(x=143, y=20)

secondEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=second)
secondEntry.place(x=203, y=20)


def submit():
    try:
        
        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please input valid numbers")
        return

    while temp >= 0:
        
        mins, secs = divmod(temp, 60)

        hours = 0
        if mins > 60:
            
            hours, mins = divmod(mins, 60)


        hour.set(" {:02d}".format(hours))
        minute.set(" {:02d}".format(mins))
        second.set(" {:02d}".format(secs))

 
        root.update()
        time.sleep(1)

        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if temp == 0:
            messagebox.showinfo("Time Countdown", "Time's up")

        
        temp -= 1


# button widget
btn = Button(root, text='Start Countdown', bd='5', command=submit)
btn.place(x=90, y=120)


root.mainloop()