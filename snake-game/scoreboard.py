from turtle import Turtle
import os

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")
cwd = os.getcwd()

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        try:
            with open("./PythonScriptsHub/snake-game/data.txt", mode="r") as f:
                self.high_score = f.read()
        except FileNotFoundError:
            self.high_score = 0
        # print(os.path.join(cwd, "snake-game", "data.txt").replace("\\", "/"))
        self.score = 0
        self.color("white")
        self.pu()
        self.ht()
        self.goto(0, 270)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("./PythonScriptsHub/snake-game/data.txt", mode="w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update()
