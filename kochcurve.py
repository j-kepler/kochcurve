import numpy as np
import matplotlib.pyplot as plt

nums_dec = []
nums_bin = []
turns = []
num = 0
number = 10 ** 7

x = 0
y = 0
pos_x = []
pos_y = []

direction = 0

for i in range (number):
    nums_dec.append (num)
    num += 1

    binary_num = bin(i)[2:]
    nums_bin.append (binary_num)

for i in (nums_bin):
    is_odd = (i.count("1") & 1) == 1
    turns.append (is_odd)
    

def curve (turns, direction, x, y):
    for r in turns:
        if r == 0:
            direction -= (np.deg2rad(60))
        elif r == 1:
            x += 1 * np.cos(direction)
            y += 1 * np.sin(direction)
            pos_x.append (x)
            pos_y.append (y)

    return pos_x, pos_y

pos_x, pos_y = curve (turns, direction, x, y)

print (f"Koch curve of {len(turns):,} points.")

plt.figure()
plt.plot(pos_x, pos_y, linewidth=0.3)
plt.grid(False)
plt.tight_layout()
plt.show()