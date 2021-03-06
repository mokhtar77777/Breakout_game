import turtle as t
from layers_of_turtle import LayersOfTurtle

FONT = ("Courier", 20, "bold")


class ScoreBoard(t.Turtle):

    def __init__(self):
        super().__init__()
        self.lives = 3
        self.score = 0
        self.penup()
        self.color("white")
        self.speed(0)
        self.hideturtle()
        self.update_score(score=self.score, lives=self.lives)

    def update_score(self, score: int, lives: int):
        self.clear()
        self.write_title()
        self.draw_barrier()
        self.goto(200, 300)
        self.write(f"Score: {score}", font=FONT)
        self.goto(-320, 300)
        self.write(f"Lives: {lives}", font=FONT)

    def draw_barrier(self):
        self.goto(350, -300)
        self.setheading(90)
        self.pendown()
        self.pensize(2)
        self.forward(580)
        self.setheading(180)
        self.pensize(2)
        self.forward(700)
        self.setheading(270)
        self.forward(580)
        self.penup()

    def write_title(self):
        self.goto(0, 300)
        self.write("BREAKOUT GAME", font=FONT, align="center")

    def write_final_score(self):
        self.goto(0, 200)
        layers_of_turtle = LayersOfTurtle()
        self.write(f"Your final score is {self.score}/{layers_of_turtle.get_number_of_turtles()}", font=FONT, align="center")
