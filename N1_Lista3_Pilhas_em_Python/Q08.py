from Pilha import Pilha

decimal = int(input("Digite o número decimal: "))
def decimal_hexadecimal(decimal):
    hexadecimal = Pilha()
    while decimal>0:
        num = decimal - (decimal//16 * 16)
        hexadecimal.inserir(num)
        decimal = decimal//16
        hexa = ""
    while not hexadecimal.is_empty():
        bit = hexadecimal.remover()
        hexa += str(bit)
    return hexa
hexadecimal = decimal_hexadecimal(decimal)
print("O número octal é:", hexadecimal)