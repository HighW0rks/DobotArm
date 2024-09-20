from RobotArm import RobotArm

robotArm = RobotArm("exercise 3")
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

x = 4
while x != 0:
    grab()
    move(1)
    drop()
    move(-1)
    x -= 1


robotArm.wait()