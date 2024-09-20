from RobotArm import RobotArm

robotArm = RobotArm("exercise 7")
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
for _ in range(5):
    for _ in range(6):
        grab()
        move(-1)
        drop()
        move(1)
    move(2)

robotArm.wait()