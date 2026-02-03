import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 100)
ex = np.exp(x)

plt.plot(x, ex, label='e^x')
plt.xlabel('x')
plt.ylabel('exp(x)')
plt.title('Exponential Function')
plt.grid(True)
plt.legend()

# Save plot instead of showing
plt.savefig("exponential_plot.png")  
print("Plot saved as 'exponential_plot.png'")
