from Pilha import Pilha

binario = input("Digite o número binário: ")
def binario_para_octal(binario):
    octal = Pilha()
    while len(binario) % 3 != 0:
        binario = '0' + binario
    for i in range(0, len(binario), 3):
        dec = binario[i:i + 3]
        decimal = int(dec, 2)
        octal.inserir(decimal)
    oct = ""
    while not octal.is_empty():
        digito = octal.remover()
        oct += str(digito)
    oct = oct[::-1]
    return oct
octal = binario_para_octal(binario)
print("O número octal é:", octal)