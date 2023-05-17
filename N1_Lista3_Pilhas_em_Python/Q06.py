def verificar_balanceamento(string):
    pilha = pilha()
    abertos = "({["
    fechados = ")}]"
    
    for char in string:
        if char in abertos:
            pilha.inserir(char)
        elif char in fechados:
            if pilha.is_empty():
                return False
            topo = pilha.topo()
            if abertos.index(topo) != fechados.index(char):
                return False
            pilha.remover()
    
    return pilha.is_empty()


string = input("Digite uma sequência de caracteres: ")
if verificar_balanceamento(string):
    print("Os caracteres estão balanceados.")
else:
    print("Os caracteres não estão balanceados.")