from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make A Bet", prompt="Which turtle would win the race? Choose a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-125, -75, -25, 25, 75, 125]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() >= 230:
            winning_turtle_color = turtle.pencolor()
            is_race_on = False

if user_bet == winning_turtle_color:
    print("You won!")
else:
    print(f"You lost! The {winning_turtle_color} turtle is the winner!")

screen.exitonclick()
