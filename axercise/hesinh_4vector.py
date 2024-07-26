import numpy as np


u1 = np.random.rand(6, 1)
u2 = np.random.rand(6, 1)
u3 = np.random.rand(6, 1)
u4 = np.random.rand(6, 1)


#chuan hoa vector u1 = 1
v1 = u1 / np.linalg.norm(u1)

#tim v2 truc chuan voi v1 voi v2 = u2 * tv1  <=> v2 = u2 - <u2, u1> * v1

v2 = u2 - np.dot(u2.T, v1) * v1

#chuan hoa v2 = 1
v2 = v2 / np.linalg.norm(v2)

#tim v3 truc chuan voi v1, v2 voi v3 = u3 -<u3, v1> *v1 - <u3, v2> * v2

v3 = u3 - np.dot(u3.T, v1) * v1 - np.dot(u3.T, v2) * v2

#chuan hoa v3 = 1
v3 = v3 / np.linalg.norm(v3)

#tim v4 truc chuan voi v1, v2, v3 voi v4 = u4 - <u4, v1> * v1 - <u4, v2> * v2 - <u4, v3> * v3
v4 = u4 - np.dot(u4.T, v1) * v1 - np.dot(u4.T, v2) * v2 - np.dot(u4.T, v3) * v3
# chuan hoa v4 
v4 = v4 / np.linalg.norm(v4)
V = np.concatenate((v1, v2, v3, v4), axis = 1)

#kiem tra V.T * V = I
test = np.dot(V.T, V)
test
