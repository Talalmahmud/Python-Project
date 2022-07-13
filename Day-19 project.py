import random
import turtle as t


screen = t.Screen()

screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")

y_position = [-70, -40, -10, 20, 50, 80]
color = ['red', 'green', 'yellow', 'blue', 'gray', 'violet']
all_turtle = []
is_race_on = False

for turtle_index in range(0, 6):
    tim = t.Turtle()
    tim.shape('turtle')
    tim.color(color[turtle_index])
    tim.penup()
    tim.goto(x=-250, y=y_position[turtle_index])
    all_turtle.append(tim)


if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! THe {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! THe {winning_color} turtle is the winner.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



# move turtle
'''def move_forward():
    tim.setheading(0)
    tim.forward(100)


def move_backward():
    tim.setheading(180)
    tim.forward(100)


def clear():
    tim.clear()
    #tim.home()


screen.listen()
screen.onkey(key='r', fun=move_forward)
screen.onkey(key='l', fun=move_backward)
screen.onkey(key='c', fun=clear)'''

screen.mainloop()