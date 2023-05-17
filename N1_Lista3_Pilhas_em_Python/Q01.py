def verificar_parenteses(expressao):
    pilha = Pilha()

    for caractere in expressao:
        if caractere == "(":
            pilha.inserir(caractere)
        elif caractere == ")":
            if pilha.is_empty() or pilha.topo() != "(":
                return False
            pilha.remover()

    return pilha.is_empty()

expressao = input("Digite a expressão matemática: ")
if verificar_parenteses(expressao):
    print("Os parênteses estão balanceados.")
else:
    print("Os parênteses não estão balanceados.")