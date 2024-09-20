from RobotArm import RobotArm

robotArm = RobotArm("exercise 8")
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

move(1)
for _ in range(7):
    grab()
    move(8)
    drop()
    move(-8)

robotArm.wait()