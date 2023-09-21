from turtle import Turtle


class Trap(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1.6, stretch_wid=0.5)
        self.color("red")
        self.set_position(coordinates)

    def set_position(self, coordinates):
        self.goto(coordinates)
