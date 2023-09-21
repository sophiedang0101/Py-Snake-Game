from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.move()

    def move(self):
        random_x = random.randint(-265, 260)
        random_y = random.randint(-265, 260)
        self.goto(random_x, random_y)
