# stopwatch.py - A simple stopwatch program
import time

# Display the program's instructions
print("Press Enter to begin. afterwards, press Enter to 'click' the stopwatch. press CTRL + C to quit.")
input() # press enter to begin
print("started.")
startTime = time.time() # Get the first lap's start time
lastTime = startTime
lapNum = 1

# Second step is to keep track of lap times
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print("Lap #%s: %s (%s)" % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time() # Reset the last lap time.
except keyboardInterrupt:
    # Handle the CTRL+C exception to keep its error from displaying.
    print('n\Done')
    
    

