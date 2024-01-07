import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np

'''
    Easy and raw visualization
'''

def plot_3d_shapes(shapes, title):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    colors = iter(plt.cm.rainbow(np.linspace(0, 1, len(shapes))))

    # Plot shapes
    for shape in shapes:
        x1, y1, z1 = shape[0]
        x2, y2, z2 = shape[1]
        color = next(colors)
        # Plot each block in the shape
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                for z in range(z1, z2 + 1):
                    ax.bar3d(x, y, z, 1, 1, 1, shade=True, color=color)

    # Set axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Set equal scaling for all axes
    ax.set_box_aspect([np.ptp(axis) for axis in [ax.get_xlim(), ax.get_ylim(), ax.get_zlim()]])

    # Set integer labels on the axes
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.zaxis.set_major_locator(MaxNLocator(integer=True))

    # Set plot title
    plt.title(title)

starting_blocks = [((1, 0, 1), (1, 2, 1)), ((0, 0, 2), (2, 0, 2)), ((0, 2, 3), (2, 2, 3)), ((0, 0, 4), (0, 2, 4)), ((2, 0, 5), (2, 2, 5)), ((0, 1, 6), (2, 1, 6)), ((1, 1, 8), (1, 1, 9))]    
settled_blocks = [((1, 0, 1), (1, 2, 1)), ((0, 0, 2), (2, 0, 2)), ((0, 2, 2), (2, 2, 2)), ((0, 0, 3), (0, 2, 3)), ((2, 0, 3), (2, 2, 3)), ((0, 1, 4), (2, 1, 4)), ((1, 1, 5), (1, 1, 6))]

plot_3d_shapes(starting_blocks, "Starting blocks")
plot_3d_shapes(settled_blocks, "Settletd blocks")

plt.show()