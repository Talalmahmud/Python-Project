import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
colours = ['green', 'red', 'blue', 'orange', 'brown', 'yellow', 'gray']
tim.shape('turtle')

tim.hideturtle()

# TODO: 1. Draw different shape
'''def draw_shape(new_sides):
    angle = 360/new_sides
    tim.color(random.choice(colours))
    for _ in range(new_sides):
        tim.forward(100)
        tim.right(angle)


for i in range(3,11):
    draw_shape(i)'''

# TODO: 2. Draw different path walk through

'''path_directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed(0)

for _ in range(30):
    tim.color(random.choice(colours))
    tim.forward(100)
    tim.setheading(random.choice(path_directions))'''

# TODO: 3. Dash line draw

'''for _ in range(7):
    tim.forward(5)
    tim.penup()
    tim.forward(5)
    tim.pendown()'''

# TODO: 4. Circle draw

tim.circle(100,)


# TODO: 5. Draw spyrogyra
tim.speed(0)
for _ in range(300):
    tim.color(random.choice(colours))
    tim.circle(100)
    tim.setheading(tim.heading() + 10)


screen.mainloop()

