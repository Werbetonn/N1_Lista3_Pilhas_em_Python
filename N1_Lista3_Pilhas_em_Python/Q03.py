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


def calcular_expressao(expressao):
    pilha = Pilha()
    for char in expressao:
        if char.isdigit():
            pilha.inserir(int(char))
        elif char in ['+', '-', '*', '/']:
            if len(pilha) < 2:
                raise ValueError("Expressão inválida")
            num2 = pilha.remover()
            num1 = pilha.remover()
            resultado = executar_operacao(num1, num2, char)
            pilha.inserir(resultado)
        else:
            raise ValueError("Expressão inválida")
    
    if len(pilha) != 1:
        raise ValueError("Expressão inválida")
    
    return pilha.topo()


def executar_operacao(num1, num2, operador):
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        return num1 / num2


expressao = input("Digite uma expressão matemática: ")
try:
    resultado = calcular_expressao(expressao)
    print("O resultado da expressão é:", resultado)
except ValueError as e:
    print("Erro:", str(e))