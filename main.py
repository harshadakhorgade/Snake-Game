from  turtle import Screen
import  time
from food import Food
from snake import Snake
from scoreboard import Scoreboard

# git init
# git branch -M main
# git add .
# git commit -m "Initial commit"
# git remote add origin https://github.com/yourusername/your-repo.git
# git push -u origin main


screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard =Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    #detect food colision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    #detect wall colision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on =False
        scoreboard.game_over()

    #Detect tail colision
    for s in snake.segment[1:]:
        if snake.head.distance(s) < 10:
            is_game_on = False
            scoreboard.game_over()







screen.exitonclick()
