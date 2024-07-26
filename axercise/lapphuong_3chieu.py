import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

def rotate_box(ax, box, T):
    # Xoay và vẽ lại hộp
    box_rotated = T @ box
    ax.clear()
    ax.grid(True)
    ax.plot3D(box_rotated[0, :], box_rotated[1, :], box_rotated[2, :], 'b-')
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])
    plt.draw()

def on_press(event, ax, box, Tx, Ty, Tz):
    if event.key == 'x':
        rotate_box(ax, box, Tx)
    elif event.key == 'y':
        rotate_box(ax, box, Ty)
    elif event.key == 'z':
        rotate_box(ax, box, Tz)

def main():
    box = np.array([
        [0, 0, 0],
        [1, 0, 0],
        [1, 1, 0],
        [0, 1, 0],
        [0, 0, 0],
        [0, 0, 1],
        [1, 0, 1],
        [1, 1, 1],
        [0, 1, 1],
        [0, 0, 1],
        [1, 0, 1],
        [1, 0, 0],
        [1, 1, 0],
        [1, 1, 1],
        [0, 1, 1],
        [0, 1, 0]
    ]).T - 0.5

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.grid(True)
    plt.subplots_adjust(bottom=0.2)

    T = np.array([
        [1.6, 0, 0],
        [0, 1.2, 0],
        [0, 0, 0.2]
    ])

    phi = 10 / 180 * np.pi

    Tz = np.array([
        [np.cos(phi), np.sin(phi), 0],
        [-np.sin(phi), np.cos(phi), 0],
        [0, 0, 1]
    ])

    Tx = np.array([
        [1, 0, 0],
        [0, np.cos(phi), np.sin(phi)],
        [0, -np.sin(phi), np.cos(phi)]
    ])

    Ty = np.array([
        [np.cos(phi), 0, np.sin(phi)],
        [0, 1, 0],
        [-np.sin(phi), 0, np.cos(phi)]
    ])

    ax.plot3D(box[0, :], box[1, :], box[2, :], 'b-')
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])

    fig.canvas.mpl_connect('key_press_event', lambda event: on_press(event, ax, box, Tx, Ty, Tz))

    plt.show()

if __name__ == "__main__":
    main()
