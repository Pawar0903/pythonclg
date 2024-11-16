import matplotlib.pyplot as plt

# Data for plotting
x = [0, 1, 2, 3, 4, 5]  # x values
y = [2 * i + 1 for i in x]  # y values based on the equation y = 2x + 1

# Create the plot
plt.plot(x, y, marker='o', color='blue', label='y = 2x + 1')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Simple Line Plot')
plt.legend()

# Show the plot
plt.grid()
plt.show()