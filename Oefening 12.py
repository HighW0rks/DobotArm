from RobotArm import RobotArm

robotArm = RobotArm("exercise 12")
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

def check_color():
    global pos
    pos += 1
    grab()
    color = robotArm.scan()
    if color != "red":
        drop()
        move(1)
    else:
        move(9 - pos + 1)
        drop()
        move(-9 + pos)

for _ in range(9):
    check_color()



robotArm.wait()