from formula import leProposicao, And, Or, Not, Implies, Equivalent

def token_And(tokens):
    return And(tokens[0], tokens[2])

def token_Or(tokens):
    return Or(tokens[0], tokens[2])

def token_Not(tokens):
    return Not(tokens[1])

def token_Implies(tokens):
    return Implies(tokens[0], tokens[2])

def token_Equivalent(tokens):
    return Equivalent(tokens[0], tokens[2])

def token_Leitura(tokens):
    return leProposicao(tokens[0])

def token_Desemp(tokens):
    return tokens[0]