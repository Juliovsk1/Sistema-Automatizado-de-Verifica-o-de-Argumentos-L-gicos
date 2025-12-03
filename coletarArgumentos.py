def parse_Formula(texto_formula):
    try:
        return expr.parseString(texto_formula, parseAll=True)[0]
    except Exception as e:
        raise ValueError(f"Erro ao analisar a fórmula: {e}")
        return None

def coletar_Argumentos():
    premissas_list = []
    print("Premissas")
    while True:
        premissa = input("Digite uma premissa(ex: P -> Q) ou aperte 0 para finalizar:: ").strip()
        if premissa == '0':
            break
        formula_obj = parse_Formula(premissa)
        if formula_obj is not None:
            premissas_list.append(formula_obj)
    
    print("\n--- COLETANDO CONCLUSÃO ---")
    c_text = input("Digite a Conclusão: ").strip()
    conclusao = parse_Formula(c_text)
    
    if not premissas_list or conclusao is None:
        print("Argumento incompleto ou inválido.")
        return None, None
        
    return premissas_list, conclusao
