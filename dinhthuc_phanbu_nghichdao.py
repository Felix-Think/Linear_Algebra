import numpy as np
def dinhthuc(A):
    # Check if A is a 1x1 matrix
    if A.size == 1:
        return A[0, 0]
    else:
        m = 0
        for i in range(len(A)):
            # Create submatrix by removing row 0 and column i
            subA = np.delete(np.delete(A, 0, axis=0), i, axis=1)
            m += A[0, i] * (-1) ** (2 + i) * dinhthuc(subA)
        return m
def phanbu(A):
    hang, cot = A.shape
    adj = np.zeros((hang, cot))


    for i in range(hang):
        for j in range(cot):
            subA = np.delete(np.delete(A, i, axis = 0), j, axis = 1)
            adj[i, j] = (-1)**(i + j) * dinhthuc(subA)

    adj = adj.T
    return adj


if __name__ == '__main__':
 
    a = np.array([[1, 3],
                  [2, -1]])

    if dinhthuc(a) == 0:
        print("Ma tran khong kha nghich!!")

    else:
        print("Ma tran co dinh thuc khac khong!", dinhthuc(a))
        A_inver = phanbu(a) / dinhthuc(a)
        print(f'Ma tran nghich dao la, \n {A_inver}')
        print()
        A_v = np.linalg.inv(a)
        A_v
