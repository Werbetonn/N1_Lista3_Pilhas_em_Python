def verificar_palindromo(string):
    pilha = pilha()
    for digito in string:
        pilha.inserir(digito)
    
    inverso = ''
    while not pilha.is_empty():
        inverso += pilha.remover()
    
    return string == inverso


string = input("Digite uma sequência de números: ")
if verificar_palindromo(string):
    print("A string é um número palíndromo.")
else:
    print("A string não é um número palíndromo.")