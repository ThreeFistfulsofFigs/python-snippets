# ============================================================================
# PROGRAMMING LANGUAGES POPULARITY BAR GRAPH
# ============================================================================
# A script to generate a bar graph visualizing the popularity of programming
# languages in 2025, based on data from index.dev (February 2025).
# Uses matplotlib with a colored bar graph to represent language popularity.
# ============================================================================

# Import required libraries
import matplotlib.pyplot as plt  # For creating and displaying the bar graph

# ============================================================================
# DATA CONFIGURATION
# ============================================================================
# Define labels and sizes for the bar graph
labels = ["Python", "C++", "Java", "C", "C#", "JavaScript", "SQL", "Go", "Delphi", "Visual Basic"]
sizes = [23.8, 11.37, 10.66, 9.84, 4.12, 3.78, 2.87, 2.26, 2.18, 2.04]

# ============================================================================
# PLOT SETUP
# ============================================================================
# Create a figure and set the window title
plt.figure(num="Programming Languages Popularity (2025)")

# Use the 'tab10' colormap to generate distinct colors for each bar
colors = plt.cm.tab10(range(len(labels)))

# ============================================================================
# BAR GRAPH CREATION
# ============================================================================
# Create the bar graph with specified parameters
# labels: Programming language names for x-axis
# sizes: Popularity percentages for bar heights
# color: Assign distinct colors from tab10 colormap
plt.bar(labels, sizes, color=colors)

# Add axis labels and title for clarity
plt.xlabel("Programming Languages")
plt.ylabel("Popularity (%)")
plt.title("Top 10 Programming Languages Popularity\n"
          "According to index.dev in February 2025")

# ============================================================================
# DISPLAY OUTPUT
# ============================================================================
# Display the bar graph
plt.show()
