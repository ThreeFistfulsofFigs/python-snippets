# ============================================================================
# PROGRAMMING LANGUAGES POPULARITY PIE CHART
# ============================================================================
# A script to generate a pie chart visualizing the popularity of programming
# languages in 2025, based on data from index.dev (February 2025).
# Uses matplotlib to create a visually appealing chart with percentage labels.
# ============================================================================

# Import required libraries
import matplotlib.pyplot as plt  # For creating and displaying the pie chart

# ============================================================================
# DATA CONFIGURATION
# ============================================================================
# Define labels and sizes for the pie chart
labels = ["Python", "C++", "Java", "C", "C#", "JavaScript", "SQL", "Go", "Delphi", "Visual Basic"]
sizes = [23.8, 11.37, 10.66, 9.84, 4.12, 3.78, 2.87, 2.26, 2.18, 2.04]
# Calculate the total sum of sizes for accurate percentage calculation
total = sum(sizes)  # ~72.9, used to scale percentages

# ============================================================================
# PLOT SETUP
# ============================================================================
# Create a figure and set the window title
plt.figure(num="Programming Languages Popularity (2025)")

# Add a title (caption) to the pie chart
plt.title("Top 10 Programming Languages Popularity \n"
          "According to index.dev in February 2025")

# ============================================================================
# PIE CHART CREATION
# ============================================================================
# Create the pie chart with specified parameters
# labels: Programming language names
# autopct: Custom function to scale normalized percentages back to original
# counterclock=False: Arrange slices clockwise
# shadow=True: Add shadow effect for visual depth
# startangle=90: Rotate chart to start at 90 degrees
# colors: Use tab10 colormap for distinct colors
plt.pie(sizes, 
        labels=labels, 
        autopct=lambda p: f'{p * total / 100:.1f}%',  # Scale normalized percentages
        counterclock=False, 
        shadow=True, 
        startangle=90, 
        colors=plt.cm.tab10(range(10)))  # Use tab10 colormap for colors

# ============================================================================
# DISPLAY OUTPUT
# ============================================================================
# Display the pie chart
plt.show()



