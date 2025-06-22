from turtle import Screen , Turtle
import time
from snake import Snake # type: ignore
from food import Food # type: ignore
from score_board import Scoreboard # type: ignore
#----------------------

screen = Screen()
screen.setup(width= 600 , height= 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
#-------------------------------
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down ,"Down")
screen.onkey(snake.left ,"Left")
screen.onkey(snake.right ,"Right")



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detection the collision of snake with the food 
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detection the collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    
    # detection collision with own tail
    for segment in snake.segments:
        if snake.head == segment:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()





screen.exitonclick()
