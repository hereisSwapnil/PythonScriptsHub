import functools
import math
from tkinter import *

root = Tk()
root.title("Calculator")

display = Entry(root, font=10)
display.grid(row=1, columnspan=6, sticky=W + E)


# get the user input and place it in the textfield


def clear() -> None:
    display.delete(0, END)


def undo() -> None:
    entire_string = display.get()
    if entire_string:
        display.delete(display.index(END) - 1)
    else:
        clear()


def get_operation(opr):
    display.insert(INSERT, opr)


def factorial(x: int) -> int:
    return math.factorial(x)


def calculate() -> None:
    try:
        result = eval(display.get())
    except SyntaxError:
        result = "Error"
    clear()
    display.insert(0, result)


# adding button to the calculator

for j in range(1, 11):
    Button(
        root, text=str(n := j % 10), command=functools.partial(display.insert, index=INSERT, string=n), width=10
    ).grid(row=(j + 5) // 3, column=(j + 2) % 3)

Button(root, text="AC", command=lambda: clear(), width=10).grid(row=5, column=1)
Button(root, text="=", command=lambda: calculate(), width=10).grid(row=5, column=2)
Button(root, text="->", command=lambda: undo(), width=10).grid(row=2, column=3)

for j in zip(
        ('+', '-', '*', '/', '.', '%', '(', ')', 'exp', 'x!', '^2'),
        ('+', '-', '*', '/', '.', '%', '(', ')', '**', 'factorial(', '**2'),
        (3, 4, 5, 5, 3, 4, 2, 2, 3, 4, 5),
        (3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5),
):
    Button(
        root, text=j[0], command=functools.partial(display.insert, index=INSERT, string=j[1]), width=10
    ).grid(row=j[2], column=j[3])

root.mainloop()
