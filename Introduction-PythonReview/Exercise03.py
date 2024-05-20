'''
Lesma
Um dos professores desta disciplina possui como hobby criar dataset dos mais diversos tipos. Datasets são conjuntos de dados X
 normalmente estruturados em tabelas que contém L
 pares de dados. 

O último dataset gerado por esse professor misterioso é sobre lesmas. A responsabilidade de capturar lesmas velozes não é uma tarefa trivial de ser resolvida, uma vez que todas as lesmas são muito lentas. Neste dataset, cada lesma é rotulada em três níveis de acordo com sua velocidade, sendo elas:

Classe 1: Velocidade menor que 10 cm/h.
Classe 2: Velocidade maior ou igual 10 cm/h e menor que 20 cm/h.
Classe 3: Velocidade maior ou igual a 20 cm/h.
Diante do exposto, vamos ajudar o nosso querido professor a implementar um programa que a lesma mais veloz de cada classe em um grupo de lesmas.

Entrada:
A primeira linha (L) representa a quantidade de lesmas, sendo que (1≤L≤100
). Cada linha subsequente apresenta as velocidades Vi
 de cada lesma, sendo estes inteiros onde (1≤Vi≤50
).

Saída:
Para cada classe, apresente a lesma com maior velocidade. Se uma determina classe não apresentar amostras, retornar o valor zero.

'''

slugNumber = int(input())

classes = [[], [], []]
fastestGroup = []

for _ in range(slugNumber):
    slugVel = int(input())
    if slugVel < 10:
        classes[0].append(slugVel)
    elif 10 <= slugVel < 20:
        classes[1].append(slugVel)
    elif slugVel >= 20:
        classes[2].append(slugVel) 

for i in range(3):
    if classes[i] == []:
        fastestGroup.append(0)
    else:
        fastest = classes[i][0]
        for vel in classes[i]:
            if vel > fastest:
                fastest = vel
        fastestGroup.append(fastest)

for i in range(3):
    print(fastestGroup[i], end=" ")






    
