# -*- coding: utf-8 -*-
# @Time    : 2023/10/7 22:43
# @Author  : 之落花--falling_flowers
# @File    : main.py
# @Software: PyCharm
import io
import tkinter as tk
import numpy as np
import torch
from PIL import Image
from torch import nn
from torch.nn import functional as f
from torchvision import transforms


class App:
    def __init__(self):
        self.net = Net()
        self.net.load_state_dict(torch.load('net.pth'))
        self.resize = transforms.Resize([28, 28], antialias=True)
        self.line_id = None
        self.line_points = []
        self.root = tk.Tk()
        self.root.title('Handwritten digit recognizer')
        self.root.resizable(width=False, height=False)
        self.canvas = tk.Canvas(height=368, width=368, relief='groove', bd=2)
        self.canvas.pack()
        self.text = tk.StringVar(self.root, 'number:')
        tk.Label(self.root, textvariable=self.text, font=('microsoft yahei', 15)).pack(side='left')
        tk.Button(self.root, text='clear', font=('microsoft yahei', 15),
                  command=lambda: self.canvas.delete(tk.ALL)).pack(side='right')
        self.canvas.bind('<Button-1>', self.set_start)
        self.canvas.bind('<B1-Motion>', self.draw_line)
        self.canvas.bind('<ButtonRelease-1>', self.end_line)
        self.root.mainloop()

    def draw_line(self, event):
        self.line_points.extend((event.x, event.y))
        if self.line_id is not None:
            self.canvas.delete(self.line_id)
        self.line_id = self.canvas.create_line(self.line_points, width=30)

    def set_start(self, event):
        self.line_points.extend((event.x, event.y))

    def end_line(self, _):
        self.line_points.clear()
        self.line_id = None
        img = np.array(Image.open(io.BytesIO(self.canvas.postscript(colormode='mono').encode('utf-8'))))[:, :, 0]
        a = self.net(self.resize(torch.tensor(img / -255 + 1)[None]).float())
        self.text.set(f'number:{int(torch.argmax(a))}')


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 6, 3)
        self.conv2 = nn.Conv2d(6, 16, 4)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = f.max_pool2d(f.relu(self.conv1(x)), 2)
        x = f.max_pool2d(f.relu(self.conv2(x)), 2)
        x = torch.flatten(x, 0)
        x = f.relu(self.fc1(x))
        x = f.relu(self.fc2(x))
        x = self.fc3(x)
        return x


def main():
    App()


if __name__ == '__main__':
    main()
