class leProposicao:
    """Representa uma proposição atômica (P, Q, R)."""
    def __init__(self, name):
        # O nome da proposição (ex: 'P')
        self.name = name

    def evaluate(self, assignment):
        """
        Avalia a proposição usando um dicionário de atribuição.
        Ex: assignment = {'P': True, 'Q': False}
        """
        if self.name not in assignment:
            raise ValueError(f"Valor de verdade para '{self.name}' não fornecido na atribuição.")
        return assignment[self.name]

    def __repr__(self):
        return self.name
    

class Implies:
    """Representa o conectivo de implicação (->). A -> B."""
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, assignment):
        """Avalia (A -> B) como (not A) or B."""
        # Avalia A
        val_left = self.left.evaluate(assignment)
        # Avalia B
        val_right = self.right.evaluate(assignment)
        
        # A implicação é FALSA apenas se (Verdadeiro -> Falso)
        return (not val_left) or val_right

    def __repr__(self):
        return f"({self.left} -> {self.right})"

class And:
    """Representa o conectivo de conjunção (&). A & B."""
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, assignment):
        """Avalia (A & B)."""
        val_left = self.left.evaluate(assignment)
        val_right = self.right.evaluate(assignment)
        return val_left and val_right

    def __repr__(self):
        return f"({self.left} & {self.right})"


class Not:
    """Representa o conectivo de negação (~). ~A."""
    def __init__(self, operand):
        self.operand = operand

    def evaluate(self, assignment):
        """Avalia (~A)."""
        val_operand = self.operand.evaluate(assignment)
        return not val_operand

    def __repr__(self):
        return f"~{self.operand}"

class Or:
    """Representa o conectivo de disjunção (|). A | B."""
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, assignment):
        """Avalia (A | B)."""
        val_left = self.left.evaluate(assignment)
        val_right = self.right.evaluate(assignment)
        return val_left or val_right

    def __repr__(self):
        return f"({self.left} | {self.right})"
    
class Equivalent:
    """Representa o conectivo de bicondicional (<->). A <-> B."""
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, assignment):
        """Avalia (A <-> B)."""
        val_left = self.left.evaluate(assignment)
        val_right = self.right.evaluate(assignment)
        return val_left == val_right

    def __repr__(self):
        return f"({self.left} <-> {self.right})"