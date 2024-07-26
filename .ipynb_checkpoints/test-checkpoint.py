import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Ma trận ánh xạ A
A = np.array([[-1.1, 1.2, 0], [1.6, -0.2, 0]])

# Tạo một tập hợp điểm trong R^3
points_R3 = np.array([[1, 2, 3], [0, -1, 3], [1, 1, 1]])  # Ví dụ điểm

# Áp dụng ánh xạ A để biến đổi các điểm sang R^2
points_R2 = A.dot(points_R3.T).T

# Vẽ không gian R^3
fig = plt.figure(figsize=(12, 6))

# Vẽ không gian R^3
ax1 = fig.add_subplot(121, projection='3d')
ax1.scatter(points_R3[:, 0], points_R3[:, 1], points_R3[:, 2], color='blue', label='R^3 Points')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('Space R^3')
ax1.legend()

# Vẽ không gian R^2
ax2 = fig.add_subplot(122)
ax2.scatter(points_R2[:, 0], points_R2[:, 1], color='red', label='R^2 Mapped Points')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title('Mapped Space R^2')
ax2.legend()

plt.tight_layout()
plt.show()


