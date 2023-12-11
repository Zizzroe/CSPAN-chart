import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Generate some example data
years = np.arange(1995, 2009, 1)
subprime_rates = np.array([5.2, 7, 7.5, 7.6, 7.5, 8, 7, 6.5, 7.5, 6, 9.5, 11, 14.5, 16, 14])
subprime_rates_reshaped = subprime_rates[:len(years)]

# Create a figure and axis
fig, ax = plt.subplots(facecolor=(0.8, 0.8, 0.8))  # Set light gray background using RGB values
ax.set_xlim(1995, 2009)
ax.set_ylim(0, 25)
ax.set_xlabel('Year')
ax.set_ylabel('Subprime Lending Rate (%)')
ax.grid(color=(0.8, 0.8, 0.8), linestyle='--', linewidth=0.5)  # Add white grid lines
line, = ax.plot([], [], lw=2)

# Initialization function
def init():
    line.set_data([], [])
    return line,

# Update function for animation
def update(frame):
    if frame < len(years) - 2:
        line.set_data(years[:frame + 1], subprime_rates_reshaped[:frame + 1])
    else:
        line.set_data(years, subprime_rates_reshaped)  # Show all data for the last frame
    return line,

# Create the animation with a slower interval (500 milliseconds) and set repeat to False
ani = FuncAnimation(fig, update, frames=len(years), init_func=init, interval=750, blit=True, repeat=False)

# Show the animation
plt.show()
