from sympy import symbols
from sympy.logic.boolalg import truth_table

A, B = symbols('A B')
expr = (A & ~B) | B

for row in truth_table(expr, [A, B]):
    print(row)
