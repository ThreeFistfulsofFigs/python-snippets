# ============================================================================
# ANIMATED SCATTER PLOT
# ============================================================================
# A script to generate an animated scatter plot with randomly moving points.
# Points are initialized with random positions, colors, and sizes, and their
# positions are updated with small random offsets in each frame.
# ============================================================================

# Import required libraries
import matplotlib.pyplot as plt  # For creating static and animated plots
import matplotlib.animation as animation  # For creating animations
import numpy as np  # For numerical operations and random data generation

# ============================================================================
# DATA CONFIGURATION
# ============================================================================
# Define constants and generate initial random data for the scatter plot
num_points = 200  # Number of points to display in the scatter plot
# Generate random x and y coordinates (range 0-10) for 'num_points' points
x, y = np.random.rand(2, num_points) * 10
# Generate random colors for each point (values between 0 and 1)
colors = np.random.rand(num_points)
# Generate random sizes for each point (scaled to 0-1000 for visibility)
sizes = np.random.rand(num_points) * 1000

# ============================================================================
# PLOT SETUP
# ============================================================================
# Create a figure and axis for the scatter plot
fig, ax = plt.subplots()  # fig: figure object, ax: axes object for plotting
# Create initial scatter plot with random points, colors, and sizes
scat = ax.scatter(x, y, c=colors, s=sizes)
# Set x and y axis limits to ensure points stay within view
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# ============================================================================
# ANIMATION FUNCTION
# ============================================================================
def animate(i):
    """
    Updates the position of scatter plot points for each animation frame.

    Args:
        i (int): Current frame number (unused directly but required by FuncAnimation)

    Returns:
        scat: Updated scatter plot object
    """
    # Update point positions by adding small random offsets to x and y
    # np.c_ combines x and y into a 2D array of shape (num_points, 2)
    # Random offsets (0 to 0.1) add subtle movement to each point
    scat.set_offsets(np.c_[x + np.random.rand(num_points) * 0.1, y + np.random.rand(num_points) * 0.1])
    return scat,  # Return the updated scatter object (required for animation)

# ============================================================================
# ANIMATION SETUP
# ============================================================================
# Create the animation
# FuncAnimation calls 'animate' for each frame, updating the plot
# frames=100: total number of frames in the animation
# interval=50: delay between frames in milliseconds (50ms = 20 frames/second)
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)

# ============================================================================
# DISPLAY OUTPUT
# ============================================================================
# Display the animated plot
plt.show()  # Show the figure window with the animated scatter plot
