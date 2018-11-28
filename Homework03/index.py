# Testing template for format function in "Stopwatch - The game"

import simplegui

###################################################
# Student should add code for the format function here

timePosition = [80,120]
scorePosition = [230,25]
maxTimerValue = 5999
curTimerValue = 0
timerInterval = 100
isTimerRunning = False
isPrintTimerDebug = True
gameCount = 0;
winCount = 0

def format(timerTicks):
    if (timerTicks < 0):
        print("Invalid input")
        return
    decimals = str(timerTicks % 10)
    seconds = doubleDigitFormat(timerTicks // 10 % 60)
    minutes = str(timerTicks // 600)
    if (len(seconds) == 1):
        seconds = "0"+seconds
    return minutes+":"+seconds+"."+decimals

def doubleDigitFormat(intInput):
    result = str(intInput)
    if (len(result) == 1):
        result = "0" + result
    return result

def tickHandler():
    global curTimerValue
    if (curTimerValue < maxTimerValue):
        curTimerValue = curTimerValue + 1
    else:
        stopTimer()
        print("Timer stopped because of maximum time reached.")
    if isPrintTimerDebug:
        print("timerDEBUG:"+str(curTimerValue))

def drawHandler(canvas):
    global gameCount
    global winCount
    timerMessage = format(curTimerValue)
    if (curTimerValue >= maxTimerValue):
        timerMessage = "Enough."
    scoreMessage = doubleDigitFormat(winCount)+"/"+doubleDigitFormat(gameCount)
    canvas.draw_text(timerMessage, timePosition, 50, "Red")
    canvas.draw_text(scoreMessage, scorePosition, 25, "White")

def startTimerHandler():
    global isTimerRunning
    global timer
    if (isTimerRunning):
        print("Timer is running already")
    else:
        timer.start()
        isTimerRunning = True
        print("Timer started")

def stopTimer():
    global isTimerRunning
    global timer
    if (isTimerRunning):
        timer.stop()
        isTimerRunning = False
        print("Timer stopped")
    else:
        print("Timer is stopped already")
        
def stopTimerHandler():
    global isTimerRunning
    global timer
    global curTimerValue
    global gameCount
    global winCount
    wasRunning = isTimerRunning
    stopTimer()
    if (wasRunning):
        print("Calculating game and win count")
        gameCount = gameCount + 1
        if (curTimerValue % 10 == 0):
            winCount = winCount+1
    else:
        print("Timer already stopped. Not calculating game and win count")


def resetTimerHandler():
    # no request to check if timer is reset on zero decimal, 
    # so not calculating it
    global isTimerRunning
    global timer
    global curTimerValue
    global gameCount
    global winCount
    stopTimer()
    curTimerValue = 0
    gameCount = 0
    winCount = 0



frame = simplegui.create_frame("TimerGame", 300, 200)
frame.set_draw_handler(drawHandler)
frame.add_button("Start", startTimerHandler, 100)
frame.add_button("Stop", stopTimerHandler, 100)
frame.add_button("Reset", resetTimerHandler, 100)
timer = simplegui.create_timer(timerInterval, tickHandler)
frame.start()

###################################################
# Test code for the format function
# Note that function should always return a string with 
# six characters


print format(0)
print format(7)
print format(17)
print format(60)
print format(63)
print format(214)
print format(599)
print format(600)
print format(602)
print format(667)
print format(1325)
print format(4567)
print format(5999)

###################################################
# Output from test

#0:00.0
#0:00.7
#0:01.7
#0:06.0
#0:06.3
#0:21.4
#0:59.9
#1:00.0
#1:00.2
#1:06.7
#2:12.5
#7:36.7
#9:59.9

