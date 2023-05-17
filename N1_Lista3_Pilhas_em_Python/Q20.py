from Pilha import Pilha

binario = input("Digite o número binário: ")
def binario_para_hexadecimal(binario):
    hexadecimal = Pilha()
    while len(binario) % 4 != 0:
        binario = '0' + binario
    for i in range(0, len(binario), 4):
        dec = binario[i:i + 4]
        decimal = int(dec, 2)
        if decimal < 10:
            hexadecimal.inserir(str(decimal))
        else:
            hexadecimal.inserir(chr(decimal + 55))
    hexa = ""
    while not hexadecimal.is_empty():
        digito = hexadecimal.remover()
        hexa += str(digito)
    hexa = hexa[::-1]
    return hexa
hexadecimal = binario_para_hexadecimal(binario)
print("O número hexadecimal é:", hexadecimal)