import time
import random
from datetime import datetime

seconds_to_wait = random.randint(2, 10)
time.sleep(seconds_to_wait)
print("PRESS ENTER!!")

i_time = datetime.now()
user_input = input()
f_time = datetime.now()

def seconds_actual_time(a_time):
    i = str(a_time).split()
    t = i[1]
    t = t.split(":")

    secs = t[2]
    return secs

i = seconds_actual_time(i_time)
f = seconds_actual_time(f_time)

reaction_time = float(f) - float(i)

print(f"Your reaction time is {reaction_time: .2f}")
