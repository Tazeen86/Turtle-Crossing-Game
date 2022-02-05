import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
sb=Scoreboard()
cars_manager=CarManager()
screen.listen()
screen.onkey(player.move,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    
    cars_manager.create_car()
    cars_manager.move_backwards()
    screen.update()
   

    for car in cars_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            sb.game_over()

    if player.ycor()>280:
        #sb.you_win()    
        player.go_to_start()
        cars_manager.level_up()
        sb.level_up()
        sb.display_score()

screen.exitonclick()
