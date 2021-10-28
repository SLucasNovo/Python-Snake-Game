# Create the snake Game

from turtle import Screen, Turtle
import time
from Snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

## Movement key binding
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ## Detect collision
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.random_spot()
        score.update_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_score()
        snake.reset()


    # Detect collision with tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment.position()) == 0:
            # game_is_on = False
            score.reset()
            snake.reset()



screen.exitonclick()


