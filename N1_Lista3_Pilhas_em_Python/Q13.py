from Pilha import Pilha

binario = input("Digite o número binário: ")
def binario_para_decimal(binario):
    num = Pilha()
    for bit in binario:
        num.inserir(int(bit))
    decimal = 0
    posicao = 0
    while not num.is_empty():
        bit = num.remover()
        decimal += bit * (2 ** posicao)
        posicao += 1
    return decimal
decimal = binario_para_decimal(binario)
print("O número decimal é:", decimal)