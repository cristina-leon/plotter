import numpy as np
from matplotlib import pyplot as plt
from sympy import lambdify, symbols

def plotter(func):
    # Define the variable
    n = symbols('n')
    
    # Convert the sympy function to a numpy-compatible function
    func_numpy = lambdify(n, func, modules='numpy')
    
    # Set plot parameters
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['text.usetex'] = True  
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath} \usepackage{amssymb}'  

    # Generate data
    x = np.arange(1, 21)
    y = func_numpy(x)

    # Scatter plot
    plt.scatter(x, y, color='red', label=r'$f(n) = \log(n+1)$')

    # Customize the axis
    ax = plt.gca()
    ax.spines['left'].set_linewidth(0.5)
    ax.spines['bottom'].set_linewidth(0.5)
    ax.set_xticks(x)
    ax.set_xlabel(r'$\mathbb{N}$', loc='right')
    ax.set_ylabel(r'$\mathbb{R}$', loc='top', rotation=0)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Add a legend
    plt.legend()

    # Show the plot
    plt.show()
