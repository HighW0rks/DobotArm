from RobotArm import RobotArm

robotArm = RobotArm("exercise 6")
robotArm.speed = 2

def move(x):
    while x < 0:
        robotArm.moveLeft()
        x += 1
    while x > 0:
        robotArm.moveRight()
        x -= 1

def grab():
    robotArm.grab()

def drop():
    robotArm.drop()

move(7)
pos_right = 1
pos_left = -2
x = 8
while x != 0:
    grab()
    move(pos_right)
    pos_right += 1
    drop()
    move(pos_left)
    pos_left -= 1
    x -= 1

robotArm.wait()