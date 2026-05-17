from sympy import *
import numpy as np

def FindDerivative():
    x = symbols('x')

    f = ((1+x)**2)/(x**3*sqrt(x+2))

    # M2
    f2 = simplify(diff(f, x, 2))
    f2_num = lambdify(x, f2, 'numpy')

    # M4
    f4 = simplify(diff(f, x, 4))
    f4_num = lambdify(x, f4, 'numpy')

    xs = np.linspace(2, 5, 10000)

    M2 = np.max(np.abs(f2_num(xs)))
    M4 = np.max(np.abs(f4_num(xs)))

    print("\nВторая производная:")
    print(simplify(diff(f, x, 2)))

    print("\nЧетвертая производная:")
    print(simplify(diff(f, x, 4)))

    print("M2 =", round(M2, 6))
    print("M4 =", round(M4, 6))