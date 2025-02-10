# utils.py
import numpy as np
import matplotlib.pyplot as plt

def plot_lines(data):
    x = data[:, 0]
    y = data[:, 1]
    plt.plot(x, y)
    plt.title('Line Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

def plot_transformation(A, e1, e2, vector_name='e'):
    color_original = "#129cab"
    color_transformed = "#cc8933"

    _, ax = plt.subplots(figsize=(7, 7))
    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)
    ax.set_xticks(np.arange(-5, 5))
    ax.set_yticks(np.arange(-5, 5))

    plt.axis([-5, 5, -5, 5])
    plt.quiver([0, 0], [0, 0], [e1[0, 0], e2[0, 0]], [e1[1, 0], e2[1, 0]], color=color_original, angles='xy', scale_units='xy', scale=1)
    plt.plot([0, e2[0, 0], e1[0, 0], e1[0, 0]],
             [0, e2[1, 0], e2[1, 0], e1[1, 0]],
             color=color_original)
    e1_sgn = 0.4 * np.array([[1] if i==0 else [i] for i in np.sign(e1.flatten())])
    ax.text(e1[0, 0]-0.2+e1_sgn[0], e1[1, 0]-0.2+e1_sgn[1], f'${vector_name}_1$', fontsize=14, color=color_original)
    e2_sgn = 0.4 * np.array([[1] if i==0 else [i] for i in np.sign(e2.flatten())])
    ax.text(e2[0, 0]-0.2+e2_sgn[0], e2[1, 0]-0.2+e2_sgn[1], f'${vector_name}_2$', fontsize=14, color=color_original)

    e1_transformed = A @ e1
    e2_transformed = A @ e2

    plt.quiver([0, 0], [0, 0], [e1_transformed[0, 0], e2_transformed[0, 0]], [e1_transformed[1, 0], e2_transformed[1, 0]],
               color=color_transformed, angles='xy', scale_units='xy', scale=1)
