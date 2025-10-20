import numpy as np
x0 = 4
y0 = 7
v0_x = 12
v0_y = 0.9
n = 100
t = np.linspase(0, 5, n)
x = x0 + v0_x * t
y = y0 + v0_y * t - (g * t**2) / 2
for i in range(n):
    print(t[i], x[i], y[i])

