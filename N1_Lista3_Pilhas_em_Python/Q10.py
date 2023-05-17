def validar_expressao(expressao):
    pilha = ()
    pares_parenteses = {'(': ')', '{': '}', '[': ']'}
    operadores = set(['+', '-', '*', '/'])

    for caractere in expressao:
        if caractere in pares_parenteses:
            pilha.append(caractere)
        elif caractere in pares_parenteses.values():
            if not pilha or caractere != pares_parenteses[pilha.pop()]:
                return False
        elif caractere in operadores:
            if len(pilha) < 2:
                return False
        else:
            continue

    return len(pilha) == 0