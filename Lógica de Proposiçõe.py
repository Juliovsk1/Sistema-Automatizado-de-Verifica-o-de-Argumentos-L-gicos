from pyparsing import Word, alphas, Literal, oneOf, infixNotation, opAssoc, ParserElement
from sympy import symbols, Not, And, Or, Implies, Equivalent
from sympy.logic.boolalg import truth_table
from formula import leProposicao, Implies, And, Not
from tokens import token_And, token_Or, token_Not, token_Implies, token_Equivalent, token_Leitura

Par_esq = Literal("(").suppress()
Par_dir = Literal(")").suppress()



ident = Word(alphas).setParseAction(token_Leitura)

AND = Literal("AND") | Literal("&")
OR = Literal("OR") | Literal("|")
NOT = Literal("NOT") | Literal("~")
EQUIVALENT = Literal("EQUIVALENT") | Literal("<->")
IMPLIES = Literal("IMPLIES") | Literal("->")

expr = infixNotation(
    ident, [(NOT, 1, opAssoc.RIGHT, token_Not), (AND, 2, opAssoc.LEFT, token_And), (OR,  2, opAssoc.LEFT, token_Or), (IMPLIES, 2, opAssoc.RIGHT, token_Implies), (EQUIVALENT, 2, opAssoc.LEFT, token_Equivalent)]
)

texto = input("Digite a proposição lógica: ")

try:
    resultado = expr.parseString(texto, parseAll=True)[0]
    print("Árvore sintática da expressão:", resultado)
except Exception as e:
    print("Expressão inválida:", e)
