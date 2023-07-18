# @TokyoEdTech Tutorial
# https://www.youtube.com/channel/UC2vm-0XX5RkWCXWwtBZGOXg

import turtle

window = turtle.Screen()
window.title("Pong by Amina Amgad")
# background color
window.bgcolor("blue")
window.setup(width=800, height=600)
# allows the game to pseed up, runs faster
window.tracer(0)

# Score
score_left = 0
score_right = 0

# Paddle on left
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.color("yellow")
paddle_left.shapesize(stretch_wid=5,stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350, 0)

# Paddle on right
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.color("green")
paddle_right.shapesize(stretch_wid=5,stretch_len=1)
paddle_right.penup()
# +ve coordinates due to wanting to go on the right side
paddle_right.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "bold"))

# Functions
# move paddle on the left up
def paddle_left_up():
    # .ycor method returns the y coordinated, assigining to variable 'y'
    y = paddle_left.ycor()
    # moeves the paddle up by 20 points
    y += 20
    paddle_left.sety(y)

# same functions as the first, but move up and down for other padels
def paddle_left_down():
    y = paddle_left.ycor()
    y -= 20
    paddle_left.sety(y)

def paddle_right_up():
    y = paddle_right.ycor()
    y += 20
    paddle_right.sety(y)

def paddle_right_down():
    y = paddle_right.ycor()
    y -= 20
    paddle_right.sety(y)

# Keyboard bindings
window.listen()
window.onkeypress(paddle_left_up, "w")
window.onkeypress(paddle_left_down, "s")
window.onkeypress(paddle_right_up, "Up")
window.onkeypress(paddle_right_down, "Down")

# main game loop, required for every game, where game runs
while True:
    #update screen while window runs
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border check
    # top
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        # reverses direction of the ball
    
    #bottom
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        # reverses direction of the ball
    
    #left
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_left += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_left, score_right), align="center", font=("Courier", 24, "bold"))
        
        # sets ball back to center and has it reverse directions

    #right
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_right += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_left, score_right), align="center", font=("Courier", 24, "bold"))
        
        # sets ball back to center and has it reverse directions
    
    # ball and paddle collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_left.ycor() + 50 and ball.ycor() > paddle_left.ycor() - 50:
        ball.dx *= -1 
    
    elif ball.xcor() > 340 and ball.ycor() < paddle_right.ycor() + 50 and ball.ycor() > paddle_left.ycor() - 50:
        ball.dx *= -1
