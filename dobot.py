
from pydobot import Dobot
from time import sleep

device = Dobot(port="COM12")
device.speed(100,100)

def move(x, y, z, suck):
    print(x,y)
    device.move_to(x=x, y=y, z=z, r=0, wait=True)
    device.suck(suck)

move(260, 0, 60, False)
while True:
    positions = [(300,20),(260,20),(220,20),(220,-20),(220,-60),(260,-60),(300,-60),(300,-20),(300,20)]
    x = 0
    for _ in range(8):
        pos = positions[x]
        move(pos[0], pos[1], 0, False)
        move(pos[0], pos[1], -50, True)
        move(pos[0], pos[1], 0, True)
        pos = positions[x+1]
        move(pos[0], pos[1], 0, True)
        move(pos[0], pos[1], -50, False)
        move(pos[0], pos[1], 0, False)
        x += 1
