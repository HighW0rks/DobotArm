from RobotArm import RobotArm

robotArm = RobotArm("exercise 10")
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

for pos in range(5):
    grab()
    move(5-pos)
    drop()
    move(-5 + pos + 1)

for pos in range(5):
    grab()
    move(-5 + pos)
    drop()
    move(5 - pos)


robotArm.wait()