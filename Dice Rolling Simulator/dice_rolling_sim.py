import tkinter as tk
import random
from PIL import Image, ImageTk

def roll_dice ():
    random_number =  random.randint(1, 6)
    result.set(random_number)
    dice_image.config(image=dice_resized_images[random_number - 1])

def roll_dice_animation(frames_left=10):
    if frames_left > 0:
        dice_image.config(image=dice_resized_images[frames_left % 6])
        root.after(200, roll_dice_animation, frames_left - 1)
    else:
        roll_dice()

root = tk.Tk()
root.title("Dice Rolling Simulator")

frame = tk.Frame(root)
frame.pack()
dice_images = [Image.open(f"./assets/dice-six-faces-{i}.png") for i in range(1, 7)]
desired_width = 100
resized_images = [img.resize((desired_width, int(img.height * (desired_width / img.width))), Image.LANCZOS) for img in dice_images]
dice_resized_images = [ImageTk.PhotoImage(img) for img in resized_images]

roll_button = tk.Button(frame, text="Roll Dice",width=20, command=roll_dice_animation)
roll_button.grid(row=0, column=0, pady=30, padx=30)
result = tk.IntVar()
dice_image = tk.Label(frame, image=dice_resized_images[0])
dice_image.grid(row=1)
output = tk.Label(frame, textvariable=result, font=("Arial", 20, "bold"), pady=10)
output.grid(row=2, column=0)
root.mainloop()