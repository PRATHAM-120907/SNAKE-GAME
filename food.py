from turtle import Turtle
import random


class Food(Turtle):#taking all the functions from the turtle module , so we don't have to make our . 
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)#length of the circle and the width of the circle
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280 , 280)
        self.goto(random_x , random_y)


        