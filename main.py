import math
import numpy as np
from matplotlib import pyplot as plt

result_list = []

def condition(n):

    if n == 1:
        result_list.append(n)
        return
    if n % 2 == 0:
        n = n // 2
        result_list.append(n)
        condition(n)
    else:
        n = n * 3 + 1
        result_list.append(n)
        condition(n)


initial_num = 775

condition(initial_num)
print(result_list)

plt.figure()
plt.plot(result_list, marker='o', linestyle='-', color='r')
plt.title(f'Collatz Sequence starting from {initial_num}')
plt.xlabel('Step')
plt.ylabel('Value')
plt.grid(True)
plt.show()


def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n  # Number of iterations before escape
        z = z * z + c
    return max_iter  # If it doesn't escape within max_iter iterations


# Function to compute the Mandelbrot set
def mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter):
    real_axis = np.linspace(x_min, x_max, width)
    imaginary_axis = np.linspace(y_min, y_max, height)
    mandelbrot_image = np.empty((height, width))

    for i in range(height):
        for j in range(width):
            c = real_axis[j] + 1j * imaginary_axis[i]
            mandelbrot_image[i, j] = mandelbrot(c, max_iter)

    return mandelbrot_image


# Initial parameters
width, height = 800, 800
x_min, x_max = -2.5, 1.5
y_min, y_max = -2, 2
max_iter = 200


# Function to update the plot after zooming
def update_plot(ax, x_min, x_max, y_min, y_max):
    # Recompute the Mandelbrot set for the zoomed region
    mandelbrot_image = mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter)

    ax.clear()
    ax.imshow(mandelbrot_image, extent=[x_min, x_max, y_min, y_max], cmap='inferno')
    ax.set_title("Mandelbrot Set")
    ax.set_xlabel("Real Axis")
    ax.set_ylabel("Imaginary Axis")
    ax.figure.canvas.draw()


# Zoom event handling
def on_zoom(event):
    if event.inaxes is None:
        return

    # Get the current limits
    ax = event.inaxes
    cur_xlim = ax.get_xlim()
    cur_ylim = ax.get_ylim()

    # Get the new limits after zooming
    if event.button == 'up':  # Zoom in
        scale_factor = 0.25
    elif event.button == 'down':  # Zoom out
        scale_factor = 2
    else:
        return

    x_min = event.xdata - (event.xdata - cur_xlim[0]) * scale_factor
    x_max = event.xdata + (cur_xlim[1] - event.xdata) * scale_factor
    y_min = event.ydata - (event.ydata - cur_ylim[0]) * scale_factor
    y_max = event.ydata + (cur_ylim[1] - event.ydata) * scale_factor

    # Update the plot with the new zoomed region
    update_plot(ax, x_min, x_max, y_min, y_max)


# Create the initial plot
fig, ax = plt.subplots()
mandelbrot_image = mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter)
img = ax.imshow(mandelbrot_image, extent=[x_min, x_max, y_min, y_max], cmap='inferno')
ax.set_title("Mandelbrot Set")
ax.set_xlabel("Real Axis")
ax.set_ylabel("Imaginary Axis")

# Connect the zoom event to the handler
fig.canvas.mpl_connect('scroll_event', on_zoom)

# Show the plot
plt.show()