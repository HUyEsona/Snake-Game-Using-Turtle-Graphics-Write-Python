from turtle import Turtle, Screen
from snake import Snake
from score_broad_game import Score_broad
from food_snake import Food
import time

screen = Screen()
screen.setup(width=600, height= 600)
screen.bgcolor('black')
screen.title('Snake Game!')
screen.tracer(0)


snake = Snake()
food = Food()
score = Score_broad()
screen.listen()
screen.onkey(fun=snake.up,key="w")
screen.onkey(fun=snake.down,key="s")
screen.onkey(fun=snake.left,key="a")
screen.onkey(fun=snake.right,key="d")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# detect collision with food
    if snake.head.distance(food) < 35:
        food.refresh()
        score.increase_score()



screen.exitonclick()