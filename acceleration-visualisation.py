import random
import os
import time

position = [0, 0]
size = [[-27, 28], [-23, 24]]
speed = [0, 0]
acceleration = [0, 0]

def clear():
    os.system("cls")

def print_info(position, speed, acceleration):
    print("position: {} speed: {} acceleration: {}\n".format(position, speed, acceleration))

def draw_board(position, size):
    x = position[0]
    y = position[1]

    for i in range(size[1][0], size[1][1]):
        for j in range(size[0][0], size[0][1]):
            if i == y and  j == x:
                print("\u2588  ", end="")
            else:
                print(".  ", end="")
            #print(str(j) + "," + str(i) + " ", end="")
        print("\n", end="")

def update_speed(speed, position, size):
    acceleration[0] = random.randint(-1,1)
    acceleration[1] = random.randint(-1,1)
    
    speed[0] = speed[0] + acceleration[0]
    speed[1] = speed[1] + acceleration[1]

    if position[0] + speed[0] > size[0][1] - 1:
        speed[0] = size[0][1] - 1 - position[0]
    elif position[0] + speed[0] < size[0][0]:
        speed[0] = size[0][0] - position[0]

    if position[1] + speed[1] > size[1][1] - 1:
        speed[1] = size[1][1] - 1 - position[1]
    elif position[1] + speed[1] < size[1][0]:
        speed[1] = size[1][0] - position[1]

    return speed, acceleration

def update_position(position, speed):
    position[0] = position[0] + speed[0]
    position[1] = position[1] + speed[1]

    return position

while True:
    clear()
    print_info(position, speed, acceleration)
    draw_board(position, size)
    time.sleep(1)
    speed, acceleration = update_speed(speed, position, size)
    position = update_position(position, speed)

