from tkinter import *
import time
import random

class Ball:
    def __init__(self, canvas, x, y, diameter, xvelocity, yvelocity, color):
        self.canvas = canvas
        self.image = canvas.create_oval(x, y, x + diameter, y + diameter, fill=color)
        self.xvelocity = xvelocity
        self.yvelocity = yvelocity
        self.diameter = diameter

    def move(self):
        coordinates = self.canvas.coords(self.image)
        if coordinates[2] >= self.canvas.winfo_width() or coordinates[0] <= 0:
            self.xvelocity = -self.xvelocity
        if coordinates[3] >= self.canvas.winfo_height() or coordinates[1] <= 0:
            self.yvelocity = -self.yvelocity
        self.canvas.move(self.image, self.xvelocity, self.yvelocity)

    def randomize_color(self):
        colors = ["white", "yellow", "orange", "red", "blue", "green", "pink", "purple"]
        new_color = random.choice(colors)
        self.canvas.itemconfig(self.image, fill=new_color)

    def randomize_velocity(self):
        self.xvelocity = random.randint(1, 10)
        self.yvelocity = random.randint(1, 10)

window = Tk()
WIDTH = 1026
HEIGHT = 310
BACKGROUND_COLOR = "#000000"

canvas = Canvas(window, bg=BACKGROUND_COLOR, width=WIDTH, height=HEIGHT)
canvas.pack()

balls = []
for _ in range(10):  # Adding 10 balls
    diameter = random.randint(30, 150)
    x = random.randint(0, WIDTH - diameter)
    y = random.randint(0, HEIGHT - diameter)
    xvelocity = random.randint(1, 10)
    yvelocity = random.randint(1, 10)
    color = random.choice(["white", "yellow", "orange", "red", "blue", "green", "pink", "purple", "cyan", "magenta"])
    ball = Ball(canvas, x, y, diameter, xvelocity, yvelocity, color)
    balls.append(ball)

while True:
    for ball in balls:
        ball.move()
        if random.random() < 0.01:
            ball.randomize_color()
        if random.random() < 0.01:
            ball.randomize_velocity()
    window.update()
    time.sleep(0.03)

window.mainloop()
