from RobotArm import RobotArm

robotArm = RobotArm("exercise 2")
robotArm.speed = 2

def move(x):
    while x < 0:
        robotArm.moveLeft()
        x += 1
    while x > 0:
        robotArm.moveRight()
        x -= 1

pickup_pos = [0, 4, 7]
drop_pos = 9

for pos in pickup_pos:
    move(pos)
    robotArm.grab()
    move(drop_pos)
    robotArm.drop()
    move(-drop_pos)
    print(pos)
robotArm.wait()