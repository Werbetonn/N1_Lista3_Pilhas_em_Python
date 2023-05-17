def inverter_ordem_palavras(string):
    palavras = string.split()
    pilha = Pilha()

    for palavra in palavras:
        pilha.inserir(palavra)

    string_invertida = ""
    while not pilha.is_empty():
        palavra = pilha.remover()
        string_invertida += palavra + " "

    return string_invertida.strip()

string = input("Digite a string: ")
string_invertida = inverter_ordem_palavras(string)
print("String invertida:", string_invertida)