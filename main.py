import random

def bubble_sort(v):
    fim = len(v)
    while fim > 0:

        i = 0
        while i < fim-1:
            if v[i] > v[i+1]:
                #realizando a troca da posição atual pela próxima
                temp = v[i]
                v[i] = v[i+1]
                v[i+1] = temp
                print(v) #mostrar a troca em tempo de execução
            i += 1
        fim -= 1

vetor = list(range(0,10))
random.shuffle(vetor)

print(vetor)    # mostrar vetor desordenado 
bubble_sort(vetor) # ordenando o vetor