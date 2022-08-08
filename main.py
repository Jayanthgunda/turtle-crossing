import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(fun=player.up, key="Up")

car_manager = CarManager()

scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.xcor() < -320:
            car_manager.all_cars.remove(car)

        if player.distance(car) < 30:
            scoreboard.game_end()
            game_is_on = False
            print(car_manager.all_cars)

    if player.ycor() > 275:
        player.setpos(0, -280)
        car_manager.increase_speed()
        scoreboard.increase_score()


screen.exitonclick()
