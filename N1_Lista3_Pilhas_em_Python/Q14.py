class Pilha:
    def __init__(self):
        self.pilha = []

    def is_empty(self):
        return len(self.pilha) == 0

    def inserir(self, valor):
        self.pilha.append(valor)

    def remover(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        return self.pilha.pop()

    def topo(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        return self.pilha[-1]


def converter_para_polonesa_reversa(expressao):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    polonesa_reversa = ''
    pilha = Pilha()

    for caractere in expressao:
        if caractere.isnumeric():
            polonesa_reversa += caractere
        elif caractere == '(':
            pilha.inserir(caractere)
        elif caractere == ')':
            while not pilha.is_empty() and pilha.topo() != '(':
                polonesa_reversa += pilha.remover()
            pilha.remover()
        else:
            while not pilha.is_empty() and pilha.topo() != '(' and precedencia[caractere] <= precedencia.get(pilha.topo(), 0):
                polonesa_reversa += pilha.remover()
            pilha.inserir(caractere)

    while not pilha.is_empty():
        polonesa_reversa += pilha.remover()

    return polonesa_reversa


expressao = input("Digite a expressão matemática: ")
polonesa_reversa = converter_para_polonesa_reversa(expressao)
print("Notação Polonesa Reversa:", polonesa_reversa)