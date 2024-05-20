"""
Implemente a função frequencia, que recebe uma mensagem e retorna o caracter mais comum dessa mensagem. Em caso de empate, retorne o primeiro caracter mais frequente

Entrada:
Sequência de caracteres em uma linha.

Saída:
O caracter com maior frequência.

Observações: Implemente apenas a função, o código de teste se encarrega de ler a entrada, chamar a função e imprimir o resultado.
"""

def frequencia(s):
    chars = list(s)
    greater = 0
    commonChar = ""

    for c in chars:
        counting = chars.count(c)
        if counting > greater:
            greater = counting
            commonChar = c
    return commonChar

print(frequencia("Estrutura de Dados"))
