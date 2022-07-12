
import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
rgb_colors = [(250, 249, 247), (243, 246, 250), (244, 251, 248), (252, 244, 248), (219, 153, 107), (133, 171, 195), (222, 72, 88), (215, 131, 149), (24, 119, 152), (241, 208, 98), (121, 177, 149), (38, 119, 84), (20, 165, 204), (219, 83, 76), (140, 86, 62), (131, 83, 102), (175, 185, 215), (21, 168, 123), (161, 209, 166), (174, 154, 74), (3, 96, 115), (237, 161, 174), (238, 166, 152), (54, 59, 93), (152, 207, 220), (102, 126, 174), (40, 56, 76), (34, 87, 53), (232, 209, 16), (74, 79, 40)]

tim.hideturtle()
tim.setheading(220)
tim.penup()
tim.forward(325)
tim.setheading(0)

for i in range(1, 101):
    tim.speed(0)
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)

    if i% 10 == 0 :
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = t.Screen()
screen.mainloop()