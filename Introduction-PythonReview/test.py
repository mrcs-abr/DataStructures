import time

def somaDeN2(n):
    inicio = time.time()

    aSoma = 0

    for i in range(1, n+1):
        aSoma = aSoma + i
    
    fim = time.time()
    
    return aSoma, fim-inicio

print(somaDeN2(100000000))


def somaDeN3(n):
    inicio = time.time()
    soma = (n*(n+1))/2
    fim = time.time()
    return  soma, fim-inicio
print(somaDeN3(1000000000))