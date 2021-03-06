import turtle as t
from scoreboard import ScoreBoard
from layers_of_turtle import LayersOfTurtle
from paddle import Paddle
from ball import Ball
import time

SCREEN_COLOR = "#2F4F4F"
COUNTING_TURTLE_FONT = ("Courier", 35, "bold")

screen = t.Screen()
screen.title("Breakout")
screen.setup(width=750, height=700)
screen.bgcolor(SCREEN_COLOR)
screen.tracer(0)
screen.listen()

counting_turtle = t.Turtle()
counting_turtle.penup()
counting_turtle.color("white")
counting_turtle.hideturtle()
counting_turtle.goto(0, 200)


def trigger_counter():
    for count in range(3, 0, -1):
        counting_turtle.clear()
        counting_turtle.write(count, font=COUNTING_TURTLE_FONT)
        screen.update()
        time.sleep(1)
    counting_turtle.clear()
    paddle.center_paddle()


score_board = ScoreBoard()
layers_of_turtle = LayersOfTurtle()
paddle = Paddle()
ball = Ball()

trigger_counter()

screen.onkeypress(key="Right", fun=paddle.move_right)
screen.onkeypress(key="Left", fun=paddle.move_left)
while True:
    time.sleep(0.001)
    screen.update()
    ball.move()
    for segment in paddle.segments_of_paddle:
        if ball.distance(segment) < 20:
            ball.change_direction_of_y()

    if ball.xcor() > 340 or ball.xcor() < -340:
        ball.change_direction_of_x()

    if ball.ycor() > 280:
        ball.change_direction_of_y()

    for turtle in layers_of_turtle.turtles:
        # print(len(layers_of_turtle.turtles))
        if ball.distance(turtle) <= 30:
            score_board.score += 1
            score_board.update_score(score=score_board.score, lives=score_board.lives)
            ball.change_direction_of_y()
            turtle.hideturtle()
            layers_of_turtle.turtles.remove(turtle)

    if ball.ycor() <= -300:
        score_board.lives -= 1
        if score_board.lives <= 0:
            break
        score_board.update_score(score=score_board.score, lives=score_board.lives)
        ball.generate_random_direction()
        trigger_counter()
        ball.goto(0, 0)

score_board.write_final_score()

screen.exitonclick()
