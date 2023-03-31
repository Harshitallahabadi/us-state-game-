import turtle
import pandas
screen=turtle.Screen()
screen.title("U.S States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data=pandas.read_csv("50_states.csv")
states=data["state"].tolist()
print(states)
g=0
answered=[]
missing_state=[]
while (g!=50):
    if (g==0):
        answer_state = screen.textinput(title="guess the state", prompt="what's another state name?")
    else:
        answer_state = screen.textinput(title=f"{g}/50", prompt="what's another state name?")
    if answer_state=="exit":
        missing_state=[state for state in states if (state.upper() not in answered)]
        miss = pandas.DataFrame(missing_state)
        a = miss.to_csv("missing_state")

        break

    print(answer_state.swapcase())
    for state in states:
        if (answer_state.swapcase() == state.upper()):
            a = data[data["state"] == state]
            x = a["x"]
            y = a["y"]
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(int(x), int(y))
            t.write(state)
            g += 1
            answered.append(state.upper())
            print(answered)




screen.exitonclick()