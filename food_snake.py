from turtle import Turtle
import random
FOOD_SHAPE = 'circle'
FOOD_COLOR = 'blue'

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.penup()
        self.color(FOOD_COLOR)
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)