import numpy as np
import matplotlib.pyplot as plt

# Create x values
x = np.linspace(-10, 10, 400)

# Define functions
linear = x
quadratic = x**2
sine = np.sin(x)

# Create subplots
plt.figure(figsize=(12, 6))

# Linear plot
plt.subplot(1, 3, 1)
plt.plot(x, linear, color='blue')
plt.title('Linear Function: y = x')
plt.grid(True)

# Quadratic plot
plt.subplot(1, 3, 2)
plt.plot(x, quadratic, color='green')
plt.title('Quadratic Function: y = x²')
plt.grid(True)

# Sine plot
plt.subplot(1, 3, 3)
plt.plot(x, sine, color='red')
plt.title('Sine Function: y = sin(x)')
plt.grid(True)

# Show all plots
plt.tight_layout()
plt.show()
