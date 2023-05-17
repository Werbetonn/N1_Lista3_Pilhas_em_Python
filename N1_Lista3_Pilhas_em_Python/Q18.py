def calcular(expressao):
    pilha = Pilha()
    operadores = {'+', '-', '*', '/'}

    for elemento in expressao.split():
        if elemento.isdigit():
            pilha.inserir(int(elemento))
        elif elemento in operadores:
            if len(pilha) < 2:
                raise ValueError("Expressão inválida")
            
            b = pilha.remover()
            a = pilha.remover()

            if elemento == '+':
                resultado = a + b
            elif elemento == '-':
                resultado = a - b
            elif elemento == '*':
                resultado = a * b
            elif elemento == '/':
                resultado = a / b

            pilha.inserir(resultado)
        else:
            raise ValueError("Elemento inválido: {}".format(elemento))

    if len(pilha) != 1:
        raise ValueError("Expressão inválida")

    return pilha.topo()

expressao = input("Digite a expressão na notação polonesa reversa: ")
resultado = calcular(expressao)
print("O resultado da expressão é:", resultado)