import turtle
import pandas


screen = turtle.Screen()
screen.title("US states game ")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)


states_data = pandas.read_csv("50_states.csv")
gussed_states = []

while len(gussed_states) < 51 :

    answer = screen.textinput(title=f"{len(gussed_states)}/50 correct States", prompt="what's the another state name ?").title()

    # if blank input is given then
    if answer == "":
        continue

    if answer == "Exit":

        # creating left states list as a return output
        left_states = []
        for s in states_data["state"]:
            if s not in gussed_states:
                left_states.append(s)

        r= pandas.DataFrame(left_states)
        r.to_csv("states_to_learn.csv")
        f = pandas.read_csv("states_to_learn.csv")
        break

    for stt in states_data["state"]:
        if answer == stt :
            if stt not in gussed_states:
                gussed_states.append(stt)


            data = states_data[states_data["state"] == stt]

            # create new turtle to write states name at its co-ordinates
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(int(data["x"]), int(data["y"]))
            t.write(stt)

