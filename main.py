import random
from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(10)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.01)
    snake.move()
    # collide with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()
    # collide with wall

    if snake.head.ycor() > 280:
        snake.head.setposition((snake.head.xcor(), -280))
    if snake.head.ycor() < -280:
        snake.head.setposition((snake.head.xcor(), 280))
    if snake.head.xcor() > 280:
        snake.head.setposition((-280, snake.head.ycor()))
    if snake.head.xcor() < -280:
        snake.head.setposition((280, snake.head.ycor()))
    # collide with tail
    for seg in snake.snake_body[1:]:

        if snake.head.distance(seg) <= 10:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
