import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.root.geometry("300x200")  # Set window dimensions

        self.label = tk.Label(root, text="Guess a number between 1 and 100:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", self.check_guess_enter)  # Bind Enter key to check_guess_enter method

        self.button = tk.Button(root, text="Submit Guess", command=self.check_guess)
        self.button.pack()

    def check_guess(self):
        self.attempt_logic()

    def check_guess_enter(self, event):
        self.attempt_logic()

    def attempt_logic(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.secret_number:
                message = "Too low! Try again."
            elif guess > self.secret_number:
                message = "Too high! Try again."
            else:
                message = f"Congratulations! You guessed the number {self.secret_number} in {self.attempts} attempts."
                self.button.config(state=tk.DISABLED)  # Disable the button after guessing correctly

            messagebox.showinfo("Result", message)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
        finally:
            self.entry.delete(0, tk.END)  # Clear the entry field

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
