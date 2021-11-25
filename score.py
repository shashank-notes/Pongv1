from turtle import Turtle


class Score(Turtle):
    def __init__(self, color,Title, x_pos):
        super().__init__()
        self.penup()
        self.score = 0
        self.hideturtle()
        self.color(color)
        self.title = Title
        self.xpos = x_pos / 2
        self.goto(self.xpos, 280)
        self.write(f"{self.score}", move=True, align="center", font=('courier', 15, 'normal'))

    def update(self):
        self.goto(self.xpos, 280)
        self.score += 1
        self.clear()
        self.write(f"{self.score}", move=True, align="center", font=('courier', 15, 'normal'))

    def gameover(self):
        self.penup()
        self.goto(0, 0)
        self.write("Game Over", move=True, align="center", font=('courier', 15, 'normal'))
