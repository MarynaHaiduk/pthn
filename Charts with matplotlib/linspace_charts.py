import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(0, 1)
Y = X ** 3 - X ** 2 - 2
plt.plot(X, Y)
plt.show()
