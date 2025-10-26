#Busca linear
def busca_linear(lista, elemento):
  for i in range(len(lista)):
    if lista[i] == elemento:
      return i
  return -1

    
