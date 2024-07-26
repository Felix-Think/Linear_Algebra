import numpy as np

# Giả sử X là ma trận dữ liệu của bạn
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Bước 1: Tính giá trị trung bình của mỗi cột
M = np.mean(X, axis=0)

# Bước 2: Tính bình phương sự chênh lệch
Y = (X - M ) ** 2

# Bước 3: Tính phương sai
variance = np.mean(Y, axis=0)
variance
# Bước 4: Tính độ lệch chuẩn
std_dev = np.sqrt(variance)

print("Giá trị trung bình của mỗi cột:", M)
print("Phương sai của mỗi cột:", variance)
print("Độ lệch chuẩn của mỗi cột:", std_dev)
