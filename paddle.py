from turtle import Turtle
import math

NO_OF_SEGMENTS = 7


class Paddle:

    def __init__(self):
        self.segments_of_paddle = []
        self.x = 0
        self.create_paddle()

    def create_paddle(self):
        for segment in range(NO_OF_SEGMENTS):
            turtle = Turtle("square")
            turtle.speed(1)
            turtle.color("white")
            turtle.penup()
            turtle.setheading(0)
            self.x = pow(-1, segment) * math.ceil(segment/2) * 20
            turtle.goto(self.x, -290)
            self.segments_of_paddle.append(turtle)

    def move_right(self):
        if self.segments_of_paddle[len(self.segments_of_paddle) - 1].xcor() <= 330:
            for segment in self.segments_of_paddle:
                segment.forward(20)

    def move_left(self):
        if self.segments_of_paddle[len(self.segments_of_paddle) - 2].xcor() >= -330:
            for segment in self.segments_of_paddle:
                segment.backward(20)

    def center_paddle(self):
        for segment_no in range(NO_OF_SEGMENTS):
            segment = self.segments_of_paddle[segment_no]
            self.x = pow(-1, segment_no) * math.ceil(segment_no / 2) * 20
            segment.goto(self.x, -290)
