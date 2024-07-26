import numpy as np

x = np.array([[1, -1, 2, -1, -1, 2],
              [2, 3, -1, 2, -2, 2],
              [0, 1, 2, 3, -1, 1]])


mean = np.mean(x, axis=1).reshape(-1, 1)
mean
# Subtract the mean from each row of x
Y = x - mean
Y 
# Multiply each element by 6


C = np.dot(Y, Y.T)
C = C * (1 / 5)

D = np.cov(x)
F = np.var(x)

