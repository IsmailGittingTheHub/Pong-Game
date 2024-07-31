from turtle import Turtle


class Paddle(Turtle):


    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)

    def go_up(self):
        x = self.xcor()
        y = self.ycor()
        y += 15
        self.goto(x, y)

    def go_down(self):
        x = self.xcor()
        y = self.ycor()
        y -= 15
        self.goto(x, y)
