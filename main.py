import sched
import time

def my_task():
    print("Task executed")


scheduler = sched.scheduler(time.time, time.sleep)
scheduler.enter(10, 1, my_task)
scheduler.run()