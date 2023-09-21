from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from trap import Trap
import time

trap_collision = False  # Flag to track collisions with traps
cooldown_counter = 0  # cooldown counter
COOLDOWN_FRAMES = 5  # a constant to set the cooldown period in terms of frames

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Awesome Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
snake_traps = []
trap_positions = []
spacing = 120

for x in range(-250 + spacing//2, 255, spacing):
    for y in range(-265 + spacing//2, 260, spacing):
        trap_positions.append((x, y))

for i in range(len(trap_positions)):
    trap = Trap(trap_positions[i])
    snake_traps.append(trap)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.move()
        snake.extend()
        scoreboard.increment_score()

    # Detect collision with wall
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or
            snake.head.ycor() > 280 or snake.head.ycor() < -280):
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

    # Detect collision with traps and remove a segment
    if cooldown_counter > 0:  # Decrease the cooldown counter if it's active
        cooldown_counter -= 1

    # Detect collision with traps only if we're not in the cooldown period
    if cooldown_counter == 0:
        for trap in snake_traps:
            if snake.head.distance(trap) < 20:
                trap_collision = True
                break

    if trap_collision:
        if len(snake.segments) > 1:
            snake.remove_segment()
            cooldown_counter = COOLDOWN_FRAMES  # Activate the cooldown
        elif len(snake.segments) == 1:
            scoreboard.reset()
            snake.reset()
        trap_collision = False  # Reset the flag

screen.exitonclick()
