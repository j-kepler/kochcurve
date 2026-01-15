import numpy as np
import matplotlib.pyplot as plt

N = 10 ** 6 + 49000

x = 0.0
y = 0.0
moves = 0

angle_index = 0
move_index = 0

angles = np.deg2rad(np.arange (6) * 60)
dx = np.cos(angles)
dy = np.sin(angles)

for i in range(N):
    moves += (i.bit_count() & 1)

pos_x = np.empty(moves, dtype=np.float32)
pos_y = np.empty(moves, dtype=np.float32)

for i in range (N):
    if i.bit_count() & 1:
        x += dx [angle_index]
        y += dy [angle_index]

        pos_x [move_index] = x
        pos_y [move_index] = y

        move_index += 1

    else:
        angle_index = (angle_index - 1) % 6

print(f"Koch curve of {N:,} points ({moves:,} segments plotted).")

plt.figure()
plt.plot(pos_x, pos_y, linewidth=0.3)
plt.axis("equal")
plt.grid(False)
plt.tight_layout()
plt.show()