from turtle import Turtle

NUMBER_OF_ROWS = 3
colors = ["red", "orange", "yellow"]


class LayersOfTurtle:

    def __init__(self):
        self.x = 290
        self.y = 150
        self.turtles = []
        self.create_layers()

    def create_layers(self):
        for color in range(NUMBER_OF_ROWS):
            self.x = 290
            while self.x >= -330:
                turtle = Turtle("turtle")
                turtle.speed(10)
                current_color = colors[color % len(colors)]
                turtle.color(current_color)
                turtle.penup()
                turtle.turtlesize(2)
                turtle.goto(self.x, self.y)
                self.turtles.append(turtle)
                self.x -= 50
            self.y -= 50

    def get_number_of_turtles(self):
        return len(self.turtles)
