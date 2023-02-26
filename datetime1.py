# Multithreading between datetime and time module
import time, datatime
startTime = datetime.datetime(2030, 10, 31, 0, 0, 0)
while datatime.now() < startTime:
    time.sleep(1) # The while loop starts a time of 1o, 31, 203, and keeps calling the time.sleep until the start time arrives.
    
print("Program now starting on Halloween 2030") # Until 10, 31, 2030; the timer will, keep iterating the time.sleep then it prints this.


