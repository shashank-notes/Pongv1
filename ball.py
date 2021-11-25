from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed('fastest')
        self.goto(0,0)
        self.x_move = 20
        self.y_move = 20
        self.pace = 0.1

    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.penup()
        self.goto(x_cor,y_cor)

    def bounce(self):
            self.y_move *= -1

    def play(self):
        self.x_move *= -1
        self.move()


    def reset(self):
        self.goto(0,0)
        self.x_move *= -1