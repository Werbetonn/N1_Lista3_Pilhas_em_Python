from Pilha import Pilha

octal = input("Digite o número octal: ")
def octal_para_decimal(octal):
    num = Pilha()
    for oct in octal:
        num.inserir(int(oct))
    decimal = 0
    posicao = 0
    while not num.is_empty():
        oct = num.remover()
        decimal += oct * (8 ** posicao)
        posicao += 1
    return decimal
decimal = octal_para_decimal(octal)
print("O número decimal é:", decimal)