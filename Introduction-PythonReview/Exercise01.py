"""
Divisores Primos
Implemente a função divisores, que recebe um número inteiro e retorna todos os seus divisores inteiros (incluindo 1 e ele mesmo) em uma lista.

Entrada da Função
Um número inteiro n>0
.

Saída da Função
Uma lista com todos os divisores desse número

Observações: Implemente apenas a função, o código de teste se encarrega de ler a entrada, chamar a função e imprimir o resultado.

"""

numList = []

def divisores(num):
    for i in range(1, num+1):
        if (num % i == 0 ):
            numList.append(i)
    return numList

print(divisores(120))

