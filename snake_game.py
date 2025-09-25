from turtle import Turtle, Screen
from snake import Snake
from score_broad_game import Score_broad
from food_snake import Food
import time

KEY_BLIND = ('w','s','a','d')

screen = Screen()
screen.setup(width=600, height= 600)
screen.bgcolor('black')
screen.title('Snake Game!')
screen.tracer(0)


snake = Snake()
food = Food()
score_broad = Score_broad()
screen.listen()
screen.onkey(fun=snake.up,key=KEY_BLIND[0])
screen.onkey(fun=snake.down,key=KEY_BLIND[1])
screen.onkey(fun=snake.left,key=KEY_BLIND[2])
screen.onkey(fun=snake.right,key=KEY_BLIND[3])


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# detect collision with food
    if snake.head.distance(food) < 35:
        food.refresh()
        snake.extend()
        score_broad.increase_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_on = False
        # score.game_over()
        score_broad.reset()
        snake.reset()

    #detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 18:
            score_broad.reset()
        

screen.exitonclick()