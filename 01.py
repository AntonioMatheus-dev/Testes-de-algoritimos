import time
import random
import numpy as np
import matplotlib.pyplot as plt

#Busca linear
def busca_linear(lista, elemento):
  for i in range(len(lista)):
    if lista[i] == elemento:
      return i
  return -1

#Busca binária
def busca_binaria(lista, elemento):
  inicio=0
  fim = len(lista)-1
  while(inicio<=fim):
    meio = (inicio + fim)//2
    if lista[meio]==elemento:
      return meio
    elif lista[meio]<elemento:
      inicio = meio + 1
    else:
      fim = meio - 1
  return -1


tamanhos = [1000, 5000, 10000, 20000,40000, 80000,100000 ]

tempos_linear_crescente = []
tempos_linear_decrescente = []
tempos_binaria_crescente = []

for tamanho in tamanhos:
    lista_aleatoria = np.random.randint(0, tamanho, tamanho)
    lista_crescente = np.sort(lista_aleatoria)
    lista_decrescente = lista_crescente[::-1]

    elemento = lista_crescente[-1]  # elemento garantido que existe

    # Linear - crescente
    inicio = time.time()
    busca_linear(lista_crescente, elemento)
    fim = time.time()
    tempos_linear_crescente.append(fim - inicio)

    # Linear - decrescente
    inicio = time.time()
    busca_linear(lista_decrescente, elemento)
    fim = time.time()
    tempos_linear_decrescente.append(fim - inicio)

    # Binária - crescente
    inicio = time.time()
    busca_binaria(lista_crescente, elemento)
    fim = time.time()
    tempos_binaria_crescente.append(fim - inicio)


# Plot do desempenho
plt.figure(figsize=(12, 6))
plt.plot(tamanhos, tempos_linear_crescente, 'o-', label='Linear (crescente)')
plt.plot(tamanhos, tempos_linear_decrescente, 'o-', label='Linear (decrescente)')
plt.plot(tamanhos, tempos_binaria_crescente, 'o-', label='Binária (crescente)')
plt.xlabel('Tamanho da Lista')
plt.ylabel('Tempo (s)')
plt.title('Comparação de desempenho de diferentes algoritimos de busca (Linear VS Binário)')
plt.legend()
plt.grid(True, ls='--', linewidth=0.5)
plt.yscale('log')
plt.show()