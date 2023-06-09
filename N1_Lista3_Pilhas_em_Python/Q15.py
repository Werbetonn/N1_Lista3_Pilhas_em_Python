class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Pilha:
    def __init__(self):
        self._topo = None
        self.tamanho = 0

    def __len__(self):
        return self.tamanho

    def is_empty(self):
        return self.tamanho == 0

    def inserir(self, valor):
        no = No(valor)
        no.proximo = self._topo
        self._topo = no
        self.tamanho += 1

    def remover(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        valor = self._topo.valor
        self._topo = self._topo.proximo
        self.tamanho -= 1
        return valor

    def topo(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        return self._topo.valor


def converter_para_binario(string):
    pilha = Pilha()

    for caractere in string:
        if caractere.isdigit():
            pilha.inserir(int(caractere))
        else:
            raise ValueError("Caractere inválido: {}".format(caractere))

    binario = ""
    while not pilha.is_empty():
        binario += str(pilha.remover())

    return binario


string = input("Digite a string contendo números: ")
binario = converter_para_binario(string)
print("Número binário convertido:", binario)