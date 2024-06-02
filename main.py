import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.spines.top'] = False

def f(x):
   return np.log(n)

x = np.linspace(0, 10, 100)

for direction in ["xzero", "yzero"]:
    plt.axis[direction].set_axisline_style("-|>")
    plt.axis[direction].set_visible(True)

plt.tick_params(labelbottom=False, labelleft=False)
plt.plot(x, f(x), color='red', label=r'$f(x)$')
plt.legend()

plt.show()