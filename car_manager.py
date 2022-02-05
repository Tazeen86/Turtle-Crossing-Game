from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self) -> None:
        super().__init__()
        self.all_cars=[]
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def create_car(self):
        choice=random.randint(1,6)
        if choice == 6:

            my_car=Turtle()
            my_car.shape("square")
            my_car.color(random.choice(COLORS))
            my_car.shapesize(1,2)
            my_car.penup()
            my_car.goto((300,random.randint(-250,250)))
            self.all_cars.append(my_car)
       
    def move_backwards(self):
        for car in self.all_cars:
             car.backward(self.car_speed)
    
    def level_up(self):
         self.car_speed += MOVE_INCREMENT
