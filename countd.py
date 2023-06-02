import datetime
import time

# Set the countdown duration
countdown_minutes = 10

# Calculate the end time by adding the countdown duration to the current time
end_time = datetime.datetime.now() + datetime.timedelta(minutes=countdown_minutes)

# Perform the countdown
while datetime.datetime.now() < end_time:
    remaining_time = end_time - datetime.datetime.now()
    timecode = remaining_time.strftime("%H:%M:%S")
    print("Countdown:", timecode)
    time.sleep(1)  # Pause for 1 second

print("Countdown finished!")
