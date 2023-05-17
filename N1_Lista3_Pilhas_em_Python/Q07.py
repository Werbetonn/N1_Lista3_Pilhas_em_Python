from Pilha import Pilha

decimal = int(input("Digite o número decimal: "))
def decimal_octal(decimal):
    octal = Pilha()
    while decimal>0:
        num = decimal - (decimal//8 * 8)
        octal.inserir(num)
        decimal = decimal//8
    oct = ""
    while not octal.is_empty():
        bit = octal.remover()
        oct += str(bit)
    return oct
octal = decimal_octal(decimal)
print("O número octal é:", octal)