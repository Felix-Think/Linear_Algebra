import numpy as np
import matplotlib.pyplot as plt

   

def baitap10c2():
    plt.close('all')
    t = np.arange(0, 5.005, 0.005)
    x = np.sin(t * 13)
    y = np.sign(np.sin(t * 41) / 2 + np.sin(t * 21 - 1) / 2)
    

    plt.figure()
    plt.subplot(3, 1, 1)
    plt.plot(t, x, 'b-')
    plt.ylim([-1.2, 1.2])

    plt.subplot(3, 1, 2)
    plt.plot(t, y, 'r-')
    plt.ylim([-1.2, 1.2])

    Rx = x + 0.2 * y
    plt.subplot(3, 1, 3)
    plt.plot(t, Rx, 'k-')

    x_clean = NoiseRemove(Rx, y)

    plt.figure()
    plt.plot(t, x_clean, 'b-')

    plt.show()

def NoiseRemove(Rx, y):
    #chuan hoa y
    Rx = Rx.T
    y = y.T

    y = y / np.linalg.norm(y)
    #truc chuan Rx voi y
    Rx = Rx - np.dot(Rx.T, y) * y
    return Rx / np.linalg.norm(Rx)

if __name__ == '__main__':
    baitap10c2()

