import pytest
from snake_main.Snake_Main import snake, Food

def SnakeStart():
    Snake = snake(600, 400, 20)
    assert Snake.segments == [(100, 100), (80, 100), (60, 100)]
    assert Snake.OldDir == "Right"
    assert Snake.NewDir == "Right"
    assert Snake.width == 600
    assert Snake.height == 400
    assert Snake.seg_size == 20


def SnakeMove():
    Snake = snake(600, 400, 20)
    Snake.move()
    assert Snake.segments[0] == (120, 100)


def FoodChecker():
    food = Food(600, 400, 20)
    assert food.position != (0, 0)


def CheckFoodPos():
    food = Food(600, 400, 20)
    initial_position = food.position
    food.GiveRandomPosSnake()
    assert food.position != initial_position

if __name__ == "__main__":
    pytest.main()
