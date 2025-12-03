from pyparsing import Word, alphas, Literal, oneOf, infixNotation, opAssoc, ParserElement
from sympy import symbols, Not, And, Or, Implies, Equivalent
from sympy.logic.boolalg import truth_table

ident = Word(alphas)

AND = Literal("AND") | Literal("&")
OR = Literal("OR") | Literal("|")
NOT = Literal("NOT") | Literal("~")
EQUIVALENT = Literal("EQUIVALENT") | Literal("<->")
IMPLIES = Literal("IMPLIES") | Literal("->")

expr = infixNotation(
    ident, [(NOT, 1, opAssoc.RIGHT), (AND, 2, opAssoc.LEFT), (OR,  2, opAssoc.LEFT), (IMPLIES, 2, opAssoc.RIGHT), (EQUIVALENT, 2, opAssoc.LEFT)]
)

texto = input("Digite a proposição lógica: ")

try:
    resultado = expr.parseString(texto, parseAll=True)
    print("Árvore sintática da expressão:")
    print(resultado)
except Exception as e:
    print("Expressão inválida:", e)
