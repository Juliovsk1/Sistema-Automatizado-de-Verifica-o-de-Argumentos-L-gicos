from pyparsing import Word, alphas, Literal, oneOf, infixNotation, opAssoc

ident = Word(alphas)

AND = Literal("AND")
OR = Literal("OR")
NOT = Literal("NOT")

expr = infixNotation(
    ident,
    [
        (NOT, 1, opAssoc.RIGHT),
        (AND, 2, opAssoc.LEFT),
        (OR,  2, opAssoc.LEFT),
    ]
)
if __name__ == "__main__":
    test_expr = "A AND NOT B OR C"
    parsed = expr.parseString(test_expr)
    print(parsed)

from sympy import symbols
from sympy.logic.boolalg import truth_table
A, B, C = symbols('A B C')
expr = (A & ~B) | C
for row in truth_table(expr, [A, B, C]):
    print(row)



