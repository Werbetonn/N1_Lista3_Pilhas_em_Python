from Pilha import Pilha

hexadecimal = input("Digite o número hexadecimal: ")
def hexadecimal_para_decimal(hexadecimal):
    num = Pilha()
    for hexa in hexadecimal:
        if hexa.isdigit():
            num.inserir(int(hexa))
        else:
            valor = ord(hexa.upper()) - ord('A') + 10
            num.inserir(valor)
    decimal = 0
    posicao = 0
    while not num.is_empty():
        hexa = num.remover()
        decimal += hexa * (16 ** posicao)
        posicao += 1
    return decimal
decimal = hexadecimal_para_decimal(hexadecimal)
print("O número decimal é:", decimal)