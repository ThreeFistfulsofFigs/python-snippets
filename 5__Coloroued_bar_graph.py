import matplotlib.pyplot as plt

labels = ["Python", "C++", "Java", "C", "C#", "JavaScript", "SQL", "Go", "Delphi", "Visual Basic"]
sizes = [23.8, 11.37, 10.66, 9.84, 4.12, 3.78, 2.87, 2.26, 2.18, 2.04]

# Create a figure and set the window title
plt.figure(num="Programming Languages Popularity (2025)")

# Use the 'tab10' colormap to generate colors for each bar
colors = plt.cm.tab10(range(len(labels)))

plt.bar(labels, sizes, color=colors)

plt.xlabel("Programming Languages")
plt.ylabel("Popularity (%)")
plt.title("Top 10 Programming Languages Popularity\n"
          "According to index.dev in February 2025")
plt.show()
