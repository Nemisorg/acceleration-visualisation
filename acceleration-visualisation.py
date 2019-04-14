import random
import os
import time

position = [0, 0]
size = [[-16, 17], [-9, 10]]
speed = [0, 0]
acceleration = [0, 0]

def clear():
    os.system("cls")

def print_info(position, speed, acceleration):
    print("position: {} speed: {} acceleration: {}\n".format(position, speed, acceleration))

def draw_board(position, size):
    x = position[0]
    y = position[1]

    for i in range(size[1][0], size[1][1]): # Make new line for every y value in size
        for j in range(size[0][0], size[0][1]): # Print dots for every x value in size on every line
            if i == y and  j == x:
                # Print white ASCII square when the dot that has to be drawn turns out to be exactly on the current position
                print("\u2588  ", end="")
            else:
                print(".  ", end="")
        print("\n", end="")

def update_speed(speed, position, size):
    acceleration[0] = random.randint(-1,1)
    acceleration[1] = random.randint(-1,1)
    
    speed[0] = speed[0] + acceleration[0]
    speed[1] = speed[1] + acceleration[1]

    # Avoiding that the position will be outside the map
    if position[0] + speed[0] > size[0][1] - 1: # Evaluating right side
        speed[0] = size[0][1] - 1 - position[0]
    elif position[0] + speed[0] < size[0][0]: # Evaluating left side
        speed[0] = size[0][0] - position[0]

    if position[1] + speed[1] > size[1][1] - 1: # Evaluating top
        speed[1] = size[1][1] - 1 - position[1]
    elif position[1] + speed[1] < size[1][0]: # Evaluating bottom
        speed[1] = size[1][0] - position[1]

    return speed, acceleration

def update_position(position, speed):
    position[0] = position[0] + speed[0]
    position[1] = position[1] + speed[1]

    return position

while True: # Refresh
    clear() # and clear screen
    print_info(position, speed, acceleration)
    draw_board(position, size)
    time.sleep(1) # Time for your brain to process the information...................... Finished already?
    speed, acceleration = update_speed(speed, position, size)
    position = update_position(position, speed)
#                 _____   _____    _____    _____           _
# |\    /|       |       |     |  |        |       |       |_|  |\   |     /\
# | \  / |       |_____  |_____|  |_____   |_____  |       | |  | \  |    /  \
# |  \/  |  _    |       |    \         |  |       |       | |  |  \ |   /----\
# |      | |_|   |_____  |     \   _____|  |_____  |_____  |_|  |   \|  /      \
#  _____     ___     _____   _______                              _____    _____
# |         /   \   |           |      \            /     /\     |     |  |
# |_____   |     |  |____       |       \    /\    /     /  \    |_____|  |_____
#       |  |     |  |           |        \  /  \  /     /----\   |    \   |
#  _____|   \___/   |           |         \/    \/     /      \  |     \  |_____