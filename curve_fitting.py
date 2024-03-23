import numpy as np
from math import *
import matplotlib.pyplot as plt

x = np.array([0.75, 2, 3,4,6,8,8.5])
y = np.array([1.2, 1.95, 2, 2.4, 2.4,2.7, 2.6])

n = 7
A = np.array([[n, sum(x), sum(x**2)],
             [sum(x), sum(x**2), sum(x**3)],
             [sum(x**2), sum(x**3), sum(x**4)]
             ])

B = np.array([sum(y), sum(x*y), sum(x**2*y)])

C=np.array([[n, sum(x)],
            [sum(x), sum(x**2)]
    ])

D = np.array([sum(y), sum(x*y)])

parabola = np.linalg.inv(A).dot(B)
linear = np.linalg.inv(C).dot(D)

print("paraboola: ",parabola)
print("linear: ",linear)



x_ = np.linspace(0,10,100)
f_par = parabola[0] + parabola[1]*x_ + parabola[2]*x_**2
f_lin = linear[0] + linear[1]*x_

for i in range(n):
    plt.plot(x[i], y[i], "ro")

plt.plot(x_, f_par)
plt.plot(x_, f_lin)
plt.grid()
plt.show()

