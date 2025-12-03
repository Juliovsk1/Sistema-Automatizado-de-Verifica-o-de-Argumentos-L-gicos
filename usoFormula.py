from formula import leProposicao, Implies, And, Not



P = leProposicao('P')
Q = leProposicao('Q')

not_Q = Not(Q)   
not_Q_and_P = And(not_Q, P) # (~Q & P)

formula_completa = Implies(P, not_Q_and_P) #P -> (~Q & P)

print(f"Fórmula representada: {formula_completa}")

assignment_1 = {
    'P': True,
    'Q': False
}

# 3. AVALIAÇÃO
resultado_1 = formula_completa.evaluate(assignment_1)
print(f"Com P={assignment_1['P']} e Q={assignment_1['Q']}, a fórmula é: {resultado_1}")

assignment_2 = {
    'P': True,
    'Q': True
}

resultado_2 = formula_completa.evaluate(assignment_2)
print(f"Com P={assignment_2['P']} e Q={assignment_2['Q']}, a fórmula é: {resultado_2}")