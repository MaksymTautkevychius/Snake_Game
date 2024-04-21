import tkinter as tk
import random
import keyboard


x = 1920
y = 1080
Pos = 20
flag = True
class Snake_Main:
    def __init__(self, width, height, seg_size):
        self.segments = [(100, 100), (80, 100), (60, 100)]
        self.OldDir = "right"
        self.NewDir = "right"
        self.width = width
        self.height = height
        self.seg_size = seg_size

    def move(self):
        head_x, head_y = self.segments[0]
        if self.NewDir == "up":
            new_head = (head_x, head_y - self.seg_size)
        elif self.NewDir == "down":
            new_head = (head_x, head_y + self.seg_size)
        elif self.NewDir == "right":
            new_head = (head_x + self.seg_size, head_y)
        elif self.NewDir == "left":
            new_head = (head_x - self.seg_size, head_y)
        self.segments = [new_head] + self.segments[:-1]
        self.OldDir = self.NewDir

    def ChangeDir(self, direction):
        self.NewDir = direction

    def Collision(self):
        head_x, head_y = self.segments[0]
        return (
            head_x in (0, self.width)
            or head_y in (0, self.height)
            or (head_x, head_y) in self.segments[1:]
        )

    def Food(self, food_position):
        return self.segments[0] == food_position

    def Grow(self):
        self.segments.append(self.segments[-1])


# Food class
class Food:
    def __init__(self, width, height, seg_size):
        self.position = (0, 0)
        self.width = width
        self.height = height
        self.seg_size = seg_size
        self.GiveRandomPosSnake()

    def GiveRandomPosSnake(self):
        x = random.randint(0, (self.width - self.seg_size) // self.seg_size) * self.seg_size
        y = random.randint(0, (self.height - self.seg_size) // self.seg_size) * self.seg_size
        self.position = (x, y)


def update():
    global flag
    if flag:
        snake.move()
        if snake.Collision():
            flag = False
        if snake.Food(food.position):
            snake.Grow()
            food.GiveRandomPosSnake()
        draw()
        root.after(100, update)
    else:
        canvas.create_text(
            x / 2, y / 2, text="Game Over!", fill="white", font=("Arial", 24)
        )


# Function to draw snake and food
def draw():
    canvas.delete("all")
    for segment in snake.segments:
        x, y = segment
        canvas.create_rectangle(
            x, y, x + Pos, y + Pos, fill="green", outline=""
        )
    x, y = food.position
    canvas.create_oval(x, y, x + Pos, y + Pos, fill="white")


def EventKey(event):
    if event.name in ["up", "w"]:
        snake.ChangeDir("up")
    elif event.name in ["down", "s"]:
        snake.ChangeDir("down")
    elif event.name in ["left", "a"]:
        snake.ChangeDir("left")
    elif event.name in ["right", "d"]:
        snake.ChangeDir("right")


root = tk.Tk()
root.title("Snake Game")
root.resizable(False, False)
canvas = tk.Canvas(root, width=x, height=y, bg="black")
canvas.pack()
snake = Snake_Main(x, y, Pos)
food = Food(x, y, Pos)
keyboard.on_press(EventKey)
root.after(100, update)
root.mainloop()
