# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
lPad = 0
rPad = 1
xPos = 0
yPos = 1
isSeedBallDrawn = False
pads = [[0+HALF_PAD_WIDTH, HEIGHT/2], [WIDTH - HALF_PAD_WIDTH, HEIGHT/2]]
ballPosStart = [WIDTH/2, HEIGHT/2]
ballPos = list(ballPosStart)
ballVel = [3, 1]
paddleStartVelocity = 4
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0
scorePosition = [[WIDTH/2-50-30,40], [WIDTH/2+50, 40]]

fieldBounds = ((PAD_WIDTH, WIDTH - PAD_WIDTH), (0, HEIGHT))

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ballPos[xPos] = ballPosStart[xPos]
    ballPos[yPos] = ballPosStart[yPos]
    ballVel[xPos] = random.randrange(120, 240)
    ballVel[yPos] = random.randrange(60, 180)
    if direction == LEFT:
        ballVel[xPos] *= -1
        print("Spawn direction is LEFT")
    else:
        print("Spawn direction is RIGHT")
    ballVel[yPos] *= -1

def isBallHitFieldY(ballPos, ballVel):
    if ((ballVel[yPos] > 0 and (ballPos[yPos] + BALL_RADIUS) >= fieldBounds[yPos][1]) or (ballVel[yPos] < 0 and (ballPos[yPos] - BALL_RADIUS) <= fieldBounds[yPos][0])):
        return True
    return False

def isBallHitFieldX(ballPos, ballVel):
    if ((ballVel[xPos] > 0 and (ballPos[xPos] + BALL_RADIUS) >= fieldBounds[xPos][1]) or (ballVel[xPos] < 0 and (ballPos[xPos] - BALL_RADIUS) <= fieldBounds[xPos][0])):
        return True
    return False

def isPadHitFieldY(padPos, padVel):
    if ((padVel > 0 and (padPos[yPos] + HALF_PAD_HEIGHT) >= fieldBounds[yPos][1]) or (padVel < 0 and (padPos[yPos] - HALF_PAD_HEIGHT) <= fieldBounds[yPos][0])):
        return True
    return False

def isPadHitByBall(padPos, ballPos, ballVel):
    if (ballVel[xPos] < 0 and padPos[xPos] < fieldBounds[xPos][0]) or ((ballVel[xPos] > 0 and padPos[xPos] > fieldBounds[xPos][1])):
        # if ball is moving towards left pad and it is left pad
        # or ball is moving towards right pad and it is right pad
        if isBallHitFieldX(ballPos, ballVel) and (ballPos[yPos] >= (padPos[yPos] - HALF_PAD_HEIGHT)) and (ballPos[yPos] <= (padPos[yPos] + HALF_PAD_HEIGHT)):
            # if it hit the field X limit but it was within pad Y limits
            return True
    return False

def moveBall(ballPos, ballVel):
    if not isSeedBallDrawn:
        return None
    if (isBallHitFieldY(ballPos, ballVel)):
        ballVel[yPos] *= -1
        print("Ball hit Y limit. Changing Y velocity")
    #if (isBallHitFieldX(ballPos, ballVel)):
    #    ballVel[xPos] *= -1
    ballPos[xPos] += (ballVel[xPos]/60)
    ballPos[yPos] += (ballVel[yPos]/60)

def movePad(curPadPosition, padVelocity):
    if (isPadHitFieldY(curPadPosition, padVelocity)):
        return None
    curPadPosition[yPos] += padVelocity

def drawBall(canvas):
    global isSeedBallDrawn
    canvas.draw_circle(ballPos, BALL_RADIUS, 2, 'Red', "White")
    isSeedBallDrawn = True

def getPadCorners(padPosData):
    padCorners = []
    padCorners.append([padPosData[xPos]-HALF_PAD_WIDTH, padPosData[yPos]-HALF_PAD_HEIGHT])
    padCorners.append([padPosData[xPos]+HALF_PAD_WIDTH, padPosData[yPos]-HALF_PAD_HEIGHT])
    padCorners.append([padPosData[xPos]+HALF_PAD_WIDTH, padPosData[yPos]+HALF_PAD_HEIGHT])
    padCorners.append([padPosData[xPos]-HALF_PAD_WIDTH, padPosData[yPos]+HALF_PAD_HEIGHT])
    return padCorners

def drawPad(canvas, padPosData):
    padCorners = getPadCorners(padPosData)
    canvas.draw_polygon(padCorners, 1, "White", "Gray")

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0;
    score2 = 0
    spawn_ball(RIGHT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_text(str(score1), scorePosition[0], 50, "Red")
    canvas.draw_text(str(score2), scorePosition[1], 50, "Red")
    drawPad(canvas, pads[lPad])
    drawPad(canvas, pads[rPad])
    movePad(pads[lPad], paddle1_vel)
    movePad(pads[rPad], paddle2_vel)
    if isPadHitByBall(pads[lPad], ballPos, ballVel) or isPadHitByBall(pads[rPad], ballPos, ballVel):
        ballVel[xPos] *= -1
        ballVel[xPos] = ballVel[xPos]+ballVel[xPos]/10
        ballVel[yPos] = ballVel[yPos]+ballVel[yPos]/10
        print("Pad hit by ball. xVelocity increased to "+str(ballVel[xPos])+" and yVelocity increased to "+ str(ballVel[yPos]))
    elif isBallHitFieldX(ballPos, ballVel):
        if ballVel[xPos] > 0:
            # if right gutter hit then right player lost turn
            print("Winner is LEFT player")
            score1 += 1
            spawn_ball(LEFT)
        else:
            # left gutter hit and then left player lost turn
            print("Winner is RIGHT player")
            score2 += 1
            spawn_ball(RIGHT)
    moveBall(ballPos, ballVel)
    drawBall(canvas)

def newGameHandler():
    new_game()

def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = paddleStartVelocity*-1
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = paddleStartVelocity
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = paddleStartVelocity*-1
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = paddleStartVelocity

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"] or key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("New Game", newGameHandler, 100)

# start frame
new_game()
frame.start()
