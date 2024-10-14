from RobotArm import RobotArm

robotArm = RobotArm()
robotArm.randomLevel(1,7)
robotArm.speed = 2
pos = 0
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

for x in range(9):
    grab()
    if robotArm.scan():
        move(x+1)
        drop()
        move(-x-1)
    else:
        break


robotArm.wait()