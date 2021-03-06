from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.kx = 0
        self.generate_random_direction()
        self.ky = 5

    def move(self):
        x = self.xcor()
        y = self.ycor()
        new_x = x + self.kx
        new_y = y - self.ky
        self.goto(new_x, new_y)

    def change_direction_of_y(self):
        self.ky *= -1
        self.move()

    def change_direction_of_x(self):
        self.kx *= -1
        self.move()

    def generate_random_direction(self):
        self.kx = 0
        while self.kx == 0:
            self.kx = random.randint(-3, 3)
