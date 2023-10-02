from tkinter import *

root = Tk()
root.geometry('540x600')

label = Label(root, text="Calculator GUI")
label.grid(row=0, column=0)

integerValue = StringVar()
integerValue.set("")  # Initially the field is empty

inputField = Entry(root, textvariable=integerValue, font="lucida 40 bold")
inputField.grid(row=1, column=0)


def get_data(e):
    global integerValue
    text = e.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(integerValue.get()))
            integerValue.set(result)
        except ZeroDivisionError:
            integerValue.set("Division by Zero")
        except Exception as e:
            integerValue.set("Error")
    elif text == "C":
        integerValue.set("")
    elif text == "<":
        current_value = integerValue.get()
        if current_value:
            new_value = current_value[:-1]
            integerValue.set(new_value)
    else:
        integerValue.set(integerValue.get() + text)


fr = Frame(root, bg='grey')

btn = Button(fr, text="9", padx=20, pady=20, font="lucida 30 bold")
btn.bind('<Button-1>', get_data)
btn.grid(row=0, column=1)

btn = Button(fr, text="8", padx=20, pady=20, font="lucida 30 bold")
btn.bind('<Button-1>', get_data)
btn.grid(row=0, column=2)

btn = Button(fr, text="7", padx=20, pady=20, font="lucida 30 bold")
btn.bind('<Button-1>', get_data)
btn.grid(row=0, column=3)

btn = Button(fr, text="6", padx=20, pady=20, font="lucida 30 bold")
btn.bind('<Button-1>', get_data)
btn.grid(row=1, column=1)

btn = Button(fr, text="5", padx=20, pady=20, font="lucida 30 bold")
btn.bind('<Button-1>', get_data)
btn.grid(row=1, column=2)

btn = Button(fr, text="4", padx=20, pady=20, font="lucida 30 bold")
btn.bind('<Button-1>', get_data)
btn.grid(row=1, column=3)

btn = Button(fr, text="3", padx=20, pady=20, font="lucida 30 bold")
btn.bind('<Button-1>', get_data)
btn.grid(row=2, column=1)

btn = Button(fr, text="2", padx=20, pady=20, font="lucida 30 bold")
btn.bind('<Button-1>', get_data)
btn.grid(row=2, column=2)

btn = Button(fr, text="1", padx=20, pady=20, font="lucida 30 bold")
btn.bind('<Button-1>', get_data)
btn.grid(row=2, column=3)

btn = Button(fr, text="0", padx=20, pady=20, font="lucida 30 bold")
btn.bind('<Button-1>', get_data)
btn.grid(row=3, column=1)

btn = Button(fr, text="*", padx=20, pady=20, font="lucida 30 bold")
btn.bind('<Button-1>', get_data)
btn.grid(row=3, column=2)

btn = Button(fr, text="=", padx=20, pady=20, font="lucida 30 bold")
btn.bind('<Button-1>', get_data)
btn.grid(row=3, column=3)

btn = Button(fr, text="/", padx=20, pady=20, font="lucida 30 bold")
btn.bind('<Button-1>', get_data)
btn.grid(row=4, column=1)

btn = Button(fr, text="+", padx=20, pady=20, font="lucida 30 bold")
btn.bind('<Button-1>', get_data)
btn.grid(row=4, column=2)

btn = Button(fr, text="-", padx=20, pady=20, font="lucida 30 bold")
btn.bind('<Button-1>', get_data)
btn.grid(row=4, column=3)

btn = Button(fr, text="C", padx=20, pady=20, font="lucida 30 bold")
btn.bind('<Button-1>', get_data)
btn.grid(row=5, column=1)

btn = Button(fr, text="<", padx=20, pady=20, font="lucida 30 bold")
btn.bind('<Button-1>', get_data)
btn.grid(row=5, column=2)

fr.grid()
root.mainloop()
