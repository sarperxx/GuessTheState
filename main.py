import turtle
import pandas
from collections import Counter
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states)< 50:
   answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
   if answer_state == "Exit":
      break
   if answer_state in all_states:
      guessed_states.append(answer_state)
      t = turtle.Turtle()
      t.hideturtle()
      t.penup()
      state_data = data[data.state == answer_state]
      t.goto(int(state_data.x), int(state_data.y))
      t.write(answer_state)
array_3 = list((Counter(all_states) - Counter(guessed_states)).elements())
df = pandas.DataFrame(array_3)
df.to_csv('unknown_states.csv', index=False)

