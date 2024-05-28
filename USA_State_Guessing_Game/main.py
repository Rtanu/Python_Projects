import turtle
import pandas


screen = turtle.Screen()
screen.title('USA STATE GAME ')
image='blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv('50_states.csv')

# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
guess_state = []
while len(guess_state)<50:
    answer_state = screen.textinput(title=f'{len(guess_state)}/50 state',prompt='Whats is another state game')


    # print(answer_state)
    data_list_state = data.state.to_list()

    guess = answer_state.title()
    x_cor=data[data.state==guess].x
    y_cor = data[data.state==guess].y
    # print(x_cor)
    if guess=='Exit':
        # state_not_guessed = []
        # for state in data_list_state:
        #     if state not in guess_state:
        #         state_not_guessed.append(state)
        state_not_guessed=[state for state in data_list_state if state not in guess_state]
        new_data=pandas.DataFrame(state_not_guessed)
        new_data.to_csv('missed.csv')
        break
    if guess in data_list_state:
        guess_state.append(guess)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(x_cor),int(y_cor))
        t.write(guess)

    # print(guess)



# turtle.mainloop()
screen.exitonclick()