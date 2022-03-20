from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
color = YELLOW
count_work_session = 0
count_break = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global count_work_session, count_break, REPS, timer
    window.after_cancel(timer)
    work_status_label.config(text="Timer\nfor\nstudy")
    canvas.itemconfig(timer_text, text="00:00")
    count_work_session = 0
    study_sprint_label.config(text=f"Count study sprint = {count_work_session}")
    count_break = 0
    count_break_label.config(text=f"Count pause breaks = {count_break}")
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():

    global REPS, color, count_work_session, count_break
    REPS += 1
    if REPS % 8 == 0:
        color = RED
        work_status_label.config(fg=color, text="Long Break 25 minutes")
        count_down(LONG_BREAK_MIN * 60)
    elif REPS % 2 == 0:
        color = RED
        work_status_label.config(fg=color, text="Short Break 5 minutes")
        count_down(SHORT_BREAK_MIN * 60)
    else:
        color = GREEN
        work_status_label.config(fg=color, text="It is Work time")
        count_down(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global count_work_session, count_break, timer
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes}:{'0' + str(seconds) if seconds < 10 else seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if REPS % 2 == 0:
            count_work_session += 1
            study_sprint_label.config(text=f"Count study sprint = {count_work_session}")
        else:
            count_break += 1
            count_break_label.config(text=f"Count pause breaks = {count_break}")




# ---------------------------- UI SETUP ------------------------------- #
# create main window with title
window = Tk()
window.title("Timer for work")
window.config(padx=50, pady=50, bg=YELLOW)

# download mail image in canvas
canvas = Canvas(width=500, height=520, bg=YELLOW, highlightthickness=0)
alarm_image = PhotoImage(file="/home/alexbor/Desktop/alarm.png")
canvas.create_image(250, 270, image=alarm_image)
timer_text = canvas.create_text(260, 400, text="00:00", font=(FONT_NAME, 50, "bold"))
canvas.grid(column=1, row=1)

# create buttons start, reset
start = Button(text="Start", padx="20", pady="8", font="16", command=start_timer)
start.grid(column=0, row=0, sticky="w")
reset = Button(text="Reset", padx="20", pady="8", font="16", command=reset_timer)
reset.grid(column=1, row=0, sticky="w")

work_status_label = Label(text="Timer\nfor\nstudy", fg=PINK, bg=YELLOW, font=(FONT_NAME, 18, "bold"))
study_sprint_label = Label(text="Count study sprint = 0", fg=PINK, bg=YELLOW, font=(FONT_NAME, 18, "bold"))
count_break_label = Label(text="Count pause breaks = 0", fg=PINK, bg=YELLOW, font=(FONT_NAME, 18, "bold"))
work_status_label.grid(column=0, row=1, sticky="w")
study_sprint_label.grid(column=0, row=2)
count_break_label.grid(column=0, row=3)

window.mainloop()
