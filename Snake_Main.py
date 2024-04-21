import random
import os
import time

def AddFood(board):
    food = [random.randint(0, len(board) - 1), random.randint(0, len(board[0]) - 1)]
    while food in snake:
        food = [random.randint(0, len(board) - 1), random.randint(0, len(board[0]) - 1)]
    return food

def Cycle(board, snake, food):
    os.system("cls" if os.name == "nt" else "clear")
    for i in range(len(board)):
        for j in range(len(board[0])):
            if [i, j] in snake:
                print("■", end="")
            elif [i, j] == food:
                print("★", end="")
            else:
                print(" ", end="")
        print()

board = [[" "] * 20 for _ in range(20)]
snake = [[10, 10]]
food = AddFood(board)
flow = "RIGHT"

while True:
    Cycle(board, snake, food)
    if flow == "UP":
        new_head = [snake[0][0] - 1, snake[0][1]]
    elif flow == "LEFT":
        new_head = [snake[0][0], snake[0][1] - 1]
    elif flow == "DOWN":
        new_head = [snake[0][0] + 1, snake[0][1]]
    elif flow == "RIGHT":
        new_head = [snake[0][0], snake[0][1] + 1]

    snake.insert(0, new_head)
    if snake[0] == food:
        food = AddFood(board)
    else:
        snake.pop()
    if (snake[0][0] < 0 or snake[0][0] >= len(board) or
            snake[0][1] < 0 or snake[0][1] >= len(board[0]) or
            snake[0] in snake[1:]):
        print("The end!")
        break
    time.sleep(0.5)
