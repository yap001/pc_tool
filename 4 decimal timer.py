import time
from tkinter import Tk, Button, Label

class Timer:
    def __init__(self):
        self.start_time = 0
        self.elapsed_time = 0
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.start_time = time.perf_counter() - self.elapsed_time
            self.is_running = True
            self.update_timer()

    def pause(self):
        if self.is_running:
            self.elapsed_time = time.perf_counter() - self.start_time
            self.is_running = False

    def update_timer(self):
        if self.is_running:
            self.elapsed_time = time.perf_counter() - self.start_time
            self.timer_label.config(text="{:.4f}".format(self.elapsed_time))
            self.timer_label.after(1, self.update_timer)

timer = Timer()

root = Tk()
root.title("Timer")
root.geometry("200x100")

start_button = Button(root, text="Start", command=timer.start)
start_button.pack()

pause_button = Button(root, text="Pause", command=timer.pause)
pause_button.pack()

timer_label = Label(root, text="0.0000")
timer_label.pack()

root.mainloop()
