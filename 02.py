import time
import random
import numpy as np
import matplotlib.pyplot as plt

#Função recursiva
def fibonacci_rec(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)
    
#Função interativa
def fibonacci_int(n):
    antPenul=0
    penul=1
    if n==0 or n==1:
        return n
    for i in range(2,n+1):
        atual=antPenul + penul
        antPenul=penul
        penul=atual
    return atual        
    

# Lista de índices de Fibonacci
tamanhos = [5, 10, 15, 20, 25, 30] 

tempos_fibonacci_rec = []
for n in tamanhos:
    inicio = time.time()
    fibonacci_rec(n)
    fim = time.time()
    tempos_fibonacci_rec.append(fim - inicio)

tempos_fibonacci_int = []
for n in tamanhos:
    inicio = time.time()
    fibonacci_int(n)
    fim = time.time()
    tempos_fibonacci_int.append(fim - inicio)



#Plote gráfico
plt.figure(figsize=(12, 6))
plt.plot(tamanhos, tempos_fibonacci_int, 'o-', label='Fibonacci (interativo)')
plt.plot(tamanhos, tempos_fibonacci_rec, 'o-', label='Fibonacci (recursivo)')
plt.xlabel('Tamanho da Lista')
plt.ylabel('Tempo (s)')
plt.title('Comparação de algoritimos fibonacci (Recursivo vs Interativo)')
plt.legend()
plt.grid(True, ls='--', linewidth=0.5)
plt.yscale('log')
plt.show()