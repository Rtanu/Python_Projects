from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    global reps
    reps=0
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text='00:00')
    check_marks.config(text='')



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps+=1
    work_sec= WORK_MIN*60
    short_break_sec= SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps%8==0:
        timer_label.config(text="Break",fg=RED)
        count_down(long_break_sec)

    elif reps%2 ==0:
        timer_label.config(text="Break",fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer
    count_minute = math.floor(count/60)
    count_seconds=(count%60)
    if count_seconds <10:
        count_seconds=f'0{count_seconds}'

    canvas.itemconfig(timer_text,text=f'{count_minute}:{count_seconds}')
    if count >0:
        timer= window.after(1000, count_down, count - 1)


    else:
        start_timer()
        marks=''
        work_session =math.floor(reps/2)
        for _ in range(work_session):
            marks+='✔'
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")

window.config(padx=100,pady=50,bg=YELLOW)
timer_label = Label(text='Timer',fg=GREEN,bg= YELLOW, highlightthickness=0,font=(FONT_NAME,30,"bold"))
timer_label.grid(row=0,column=1)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=tomato_image)
timer_text= canvas.create_text(100,130,text='00:00',fill='white',font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

start_button = Button(text='Start',command=start_timer)
start_button.grid(row=2,column = 0)

reset_button = Button(text="Reset",command=timer_reset)
reset_button.grid(row=2 , column=2)

check_marks = Label( fg=GREEN, bg= YELLOW,highlightthickness=0,font=(FONT_NAME,18,"bold"))
check_marks.grid(row=3,column=1)





window.mainloop()