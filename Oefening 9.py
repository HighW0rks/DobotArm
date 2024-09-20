from RobotArm import RobotArm

robotArm = RobotArm("exercise 9")
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

stapel = 1

for _ in range(4):
    for _ in range(stapel):
        if stapel == 5:
            break
        grab()
        move(5)
        drop()
        move(-5)
    stapel += 1
    move(1)
robotArm.wait()