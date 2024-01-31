from turtle import Turtle


class Paddle(Turtle):

    def __init__(self,x_cor):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(x_cor, 0)
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)
