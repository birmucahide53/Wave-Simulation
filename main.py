import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider

A_init = 10   # Amplitude
k_init = 2 * np.pi  # Wave number
f_init = 1   # Frequency
w_init = 2 * np.pi * f_init  # Rate of change of the wave (Angular frequency)

x_values = np.linspace(0, 10, 100)

def wave_equation(x, t, A, k, w): # Calculate the value on the y-axis
    return A * np.sin(k * x - w * t)

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.3)
ax.set_xlim(0, 10)
ax.set_ylim(-A_init - 2, A_init + 2)
ax.set_xlabel("Time")
ax.set_ylabel("Amplitude")
ax.set_title("Wave Simulation")
ax.grid(True)

line, = ax.plot([], [], lw=5) # Initial line

# Slider controls
ax_A = plt.axes([0.2, 0.15, 0.8, 0.03])  # Amplitude
ax_k = plt.axes([0.2, 0.10, 0.8, 0.03])  # Wave number
ax_f = plt.axes([0.2, 0.05, 0.8, 0.03])  # Frequency

slider_A = Slider(ax_A, "Amplitude (A)", 0.1, 20, valinit=A_init)
slider_k = Slider(ax_k, "Wave Number (k)", 0.1, 4 * np.pi, valinit=k_init)
slider_f = Slider(ax_f, "Frequency (f)", 0.1, 5, valinit=f_init)

def update(frame):
    A = slider_A.val
    k = slider_k.val
    f = slider_f.val
    w = 2 * np.pi * f
    y_values = wave_equation(x_values, frame * 0.1, A, k, w)
    line.set_data(x_values, y_values)
    ax.set_ylim(-A - 2, A + 2)  # Dynamically adjust the scale
    return line,

# Start the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()