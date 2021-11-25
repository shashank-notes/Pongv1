from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

# Setting up screen or Play zone
active_server = "Right"
zone = Screen()
ball = Ball()
zone.setup(width=800, height=600)
zone.bgcolor("black")
zone.title("Pong v 1.0")
zone.tracer(0)

l_score = Score("green","Left",-350)
l_paddle = Paddle(-350, 0,"green")
r_score = Score("green","Right",350)
r_paddle = Paddle(350, 0,"blue")



zone.listen()
zone.onkey(r_paddle.go_up, "Up")
zone.onkey(r_paddle.go_down, "Down")
zone.onkey(l_paddle.go_up, "w")
zone.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    ball.move()
    time.sleep(ball.pace)
    zone.update()
    # check if it touches any of the top or bottom surface
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
        zone.update()
    # check for collision with either of paddle
    if (ball.distance(r_paddle) < 61 and ball.xcor() > 320) :
        ball.play()
        r_score.update()
        zone.update()
    elif (ball.distance(l_paddle) < 61 and ball.xcor() < -320):
        ball.play()
        l_score.update()
        zone.update()
    # check ball for missing the paddle and touching the back
    # ball misses the right paddle.
    if ball.xcor() > 360:
        ball.reset()
        zone.update()

    if ball.xcor() < -360:
        ball.reset()
        zone.update()

    if l_score.score >20 or r_score.score>20:
        game_is_on = False
        l_score.gameover()
        print (f'Final Scores :  Left - {l_score.score} Right -{r_score.score}')

zone.exitonclick()
