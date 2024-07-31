from turtle import Turtle
STARTING_POSITION = (0, 0)
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(STARTING_POSITION)
        self.x_move = 15
        self.y_move = 15
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        # self.setheading(45)
        # self.forward(10)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(STARTING_POSITION)
        self.move_speed = 0.1
        self.bounce_x()