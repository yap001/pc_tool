import os
import time

while True:
    current_time = time.strftime("%H:%M:%S")
    if current_time == "12:00:00":
        os.system("shutdown /s /t 1") # shuts down the computer in 1 second
        break
    time.sleep(1)
