from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Verdana"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_txt, text="00:00")
    timer_label.config(text="Timer")
    tick.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        countdown(long_break)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        countdown(short_break)
    else:
        timer_label.config(text="Work", fg=GREEN)
        countdown(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(count):
    min = math.floor(count / 60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_txt, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1) # time in millisecond 1000ms = 1s
    else:
        start_timer()
        marks = ""
        work = math.floor(reps / 2)
        for _ in range(work):
            marks += "✔"
        tick.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 34, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_txt = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

start_btn = Button(text="Start", command=start_timer)
start_btn.grid(row=2, column=0)
reset_btn = Button(text="Reset", command=reset_timer)
reset_btn.grid(row=2, column=2)

tick = Label(fg=GREEN, bg=YELLOW)
tick.grid(row=3, column=1)


window.mainloop()
