from Pilha import Pilha

decimal = int(input("Digite o número decimal: "))
def decimal_binario(decimal):
    binario = Pilha()
    while decimal > 0:
        num = decimal - (decimal //2 * 2)
        binario.inserir(num)
        decimal = decimal//2
    bin = ""
    while not binario.is_empty():
        bit = binario.remover()
        bin += str(bit)
    return bin
binario = decimal_binario(decimal)
print("O número binário é:", binario)