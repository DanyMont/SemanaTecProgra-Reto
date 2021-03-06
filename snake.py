"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

Daniel Montero, Luis Javier Alonso and Ximena Flores 
"""

from turtle import *
import random
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
"Added solors so that the game can change snake and food color"
colors = ['black', 'orange', 'purple', 'blue', 'green']
snakecolor = 'black'
foodcolor = 'green'

def choose_color(snakecolor, foodcolor):
    "Tell Python to choose a random color from the list 'colors'"
    snakecolor = random.choice(colors)
    foodcolor = random.choice(colors)
    
    "Check if food and snake colors are equal, if so change food color"
    if foodcolor == snakecolor:
        foodcolor = random.choice(colors)
            
    return snakecolor, foodcolor

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -240 < head.x < 230 and -240 < head.y < 230

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)
        food.x = randrange(-1, 1) * 10
        food.y = randrange(-1, 1) * 10


    clear()

    for body in snake:
        square(body.x, body.y, 9, snakecolor)

    square(food.x, food.y, 9, foodcolor)
    update()
    ontimer(move, 100)

setup(500, 500, 370, 0)
hideturtle()
snakecolor, foodcolor = choose_color(snakecolor, foodcolor)
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
