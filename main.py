import numpy as np 
import matplotlib.pyplot as plt 


x = np.linspace(-10, 10, 100)
y = np.sin(x)
plt.subplot(1,2,1)
plt.plot(x, y)

plt.subplot(1,2,2)
plt.scatter(x, y)

plt.show()


