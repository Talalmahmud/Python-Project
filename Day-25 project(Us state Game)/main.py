import turtle as t
import pandas

screen = t.Screen()

screen.title("U.S.A. state Game")

image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)




data = pandas.read_csv("50_states.csv")

all_state = data.state.to_list()
guess_state = []
while len(guess_state) < 50:
    answer_state = (t.textinput(f"{len(guess_state)}/50 corrects", "Which state is next?")).title()

    if answer_state in all_state:
        guess_state.append(answer_state)
        state = t.Turtle()
        state.hideturtle()
        state.penup()

        state_name = data[data.state == answer_state]
        state.goto(int(state_name.x), int(state_name.y))
        state.write(answer_state)




'''def mouse_on_click(x, y):
    print(x, y)

t.onscreenclick(mouse_on_click)
screen.mainloop()'''

screen.mainloop()