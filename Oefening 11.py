from RobotArm import RobotArm

robotArm = RobotArm("exercise 11")
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

def check_color():
    grab()
    color = robotArm.scan()
    if color != "white":
        drop()
        move(1)
    else:
        move(1)
        drop()
        move(1)

for _ in range(9):
    check_color()


robotArm.wait()