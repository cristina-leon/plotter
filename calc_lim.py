from sympy import symbols, limit 

def calc_limit(func):
    n = symbols('n')
    func_limit = limit(func, n, float('inf'))
    print(f"The limit of the function as n approaches infinity is: {func_limit}")
    return func_limit
