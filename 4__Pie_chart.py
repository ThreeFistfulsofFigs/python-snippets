import matplotlib.pyplot as plt

labels = ["Python", "C++", "Java", "C", "C#", "JavaScript", "SQL", "Go", "Delphi", "Visual Basic"]
sizes = [23.8, 11.37, 10.66, 9.84, 4.12, 3.78, 2.87, 2.26, 2.18, 2.04]
total = sum(sizes)  # ~72.9, used to scale percentages

# Create a figure and set the window title
plt.figure(num="Programming Languages Popularity (2025)")

# Add a title (caption) to the pie chart
plt.title("Top 10 Programming Languages Popularity \n"
          "According to index.dev in February 2025")

# Create the pie chart
plt.pie(sizes, 
        labels=labels, 
        autopct=lambda p: f'{p * total / 100:.1f}%',  # Scale normalized percentages back to original
        counterclock=False, 
        shadow=True, 
        startangle=90, 
        colors=plt.cm.tab10(range(10)))  # Use tab10 colormap for colors

plt.show()



