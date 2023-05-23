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
check = '✓'
reps = 0
timer = None


# fg to change text color


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text, text='00:00')
    title.config(text='Timer')
    check_marks.config(text=' ')
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    sb_sec = SHORT_BREAK_MIN * 60
    lb_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        title.config(text="Break", fg=RED, font=(FONT_NAME, 50))
        countdown_timer(lb_sec)
    elif reps % 2 == 0 and reps % 8 != 0:
        title.config(text="Break", fg=PINK, font=(FONT_NAME, 50))
        countdown_timer(sb_sec)
    else:
        title.config(text="Work", fg=GREEN, font=(FONT_NAME, 50))
        countdown_timer(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown_timer(count):
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)
    if count_sec <= 9:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(canvas_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, countdown_timer, count - 1)
    else:
        start_timer()
        marks = " "
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += check
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title.grid(column=1, row=0)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=1, row=1)
canvas_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))

start_button = Button(text='Start', command=start_timer)
reset_button = Button(text='Reset', command=reset)

check_marks = Label(text=' ', fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=4)

start_button.grid(column=0, row=3)
reset_button.grid(column=3, row=3)
window.mainloop()
