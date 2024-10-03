import turtle
import random
import time

score = 0

screen = turtle.Screen()
screen.title("Catch The Turtle")
screen.bgcolor("Light Green")
screen.setup(width=600,height=600)

mert = turtle.Turtle()
mert.shape("turtle")
mert.color("Red")
mert.penup()
mert.speed(0)

score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0,260)
score_display.write(f"Puan : {score}", align="center", font=("Lexend", 24 , "normal"))

def on_click(x, y):
    global score
    score += 1
    score_display.clear()
    score_display.write(f"Puan : {score}", align="center", font=("Lexend", 24, "normal"))
    move_turtle()


def turtle_move():
    x = random.randint(-250, 250 )
    y = random.randint(-250, 250 )
    mert.goto(x, y)

turtle.onscreenclick(on_click)

start_time = time.time()
game_duration = 10

while time.time() - start_time < game_duration :
    turtle_move()
    time.sleep(1)

score_display.clear()
score_display.goto(0,250)
score_display.write(f"Oyun Bitti! Puanınız: {score}", align="center", font=("Gotham", 24, "normal"))

screen.mainloop()


