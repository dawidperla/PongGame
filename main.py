from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_pad = Paddle((350, 0))
l_pad = Paddle((-350, 0))
ball = Ball()
board = Scoreboard()


screen.listen()
screen.onkey(r_pad.go_up,"Up")
screen.onkey(r_pad.go_down,"Down")
screen.onkey(l_pad.go_up,"w")
screen.onkey(l_pad.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    # Detect collision with a wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #need bounce
        ball.bounce_y()

    #detect collision with the paddle r
    if ball.distance(r_pad) < 50 and ball.xcor() > 320 or ball.distance(l_pad) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    if ball.xcor() > 380:
        ball.reset_position()
        board.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        board.r_point()





screen.exitonclick()