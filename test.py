import numpy as np
import matplotlib.pyplot as plt

#Create house 2D

house = np.array([[0, 0],
                  [4, 0],
                  [4, 1],
                  [3, 2],
                  [1, 2],
                  [0, 1],
                  [0, 0],
                  [2, 0],
                  [2, 1],
                  [3, 2],
                  [4, 1],
                  [0, 1]])

window = np.array([[0.5, 0.75],
                   [1, 0.75],
                   [1, 0.25],
                   [0.5, 0.25],
                   [0.5, 0.75]])
plt.plot(house[:, 0], house[:, 1], 'b-')
plt.plot(window[:, 0], window[:, 1], 'r-')

A = np.array([[-2, 0.3], [0.6, -1]])

new_house = np.dot(A, house.T).T
new_window = np.dot(A, window.T).T

plt.plot(new_house[:, 0], new_house[:, 1], 'g-')
plt.plot(new_window[:, 0], new_window[:, 1], 'y-')
