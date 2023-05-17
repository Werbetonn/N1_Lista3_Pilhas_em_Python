class Pilha:
    def __init__(self):
        self._topo = None
        self.tamanho = 0
   
    def __len__(self):
        return self.tamanho
   
    def is_empty(self):
        return self.tamanho == 0
   
    def inserir(self, valor):
        no = no(valor)
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


def verificar_palindromo(string):
    pilha = Pilha()
    for char in string:
        pilha.inserir(char)
    
    inverso = ''
    while not pilha.is_empty():
        inverso += pilha.remover()
    
    return string == inverso


string = input("Digite uma sequência de caracteres: ")
if verificar_palindromo(string):
    print("A string é um palíndromo.")
else:
    print("A string não é um palíndromo.")