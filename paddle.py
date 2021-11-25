from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos,y_pos,color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.resizemode('user')
        self.penup()
        self.speed('fastest')
        self.goto(x_pos,y_pos)
        self.shapesize(5, 1, 0)


    def go_up(self):
        new_y = self.ycor() + 25
        if new_y < 275:
           self.goto(self.xcor(), new_y)


    def go_down(self):
        new_y = self.ycor() - 25
        if new_y >-275:
            self.goto(self.xcor(), new_y)