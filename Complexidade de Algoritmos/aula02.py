
def inverter_lista(lista):
    tamanho = len(lista)
    limite = tamanho//2
    for i in range(limite):
      aux = lista[i]
      lista[i] = lista[n-i]
      lista[tamanho-i] = aux

# O parametro lista é chamada de entrada do algoritmo e a lista invertida (resultado) é chamada de saída do algoritmo
# 4 + N complexidade de espaço
# 2 + 2N complexidade de tempo = O(n)
# Tanto para complexidade de tempo quanto de espaço, depende do tamanho da lista (N)

def inverter_lista2(lista):
    nova_lista = []
    tamanho = len(lista)
    for i in range(tamanho):
      nova_lista.append(lista[tamanho-i])
    return nova_lista
  
# 2 + N complexidade de tempo
# 3 + 2*N complexidade de espaço

def tem_duplicados(lista):
    for i in range(len(lista)-1):
      for j in range(i+1, len(lista)):
        if lista[i] == lista[j]:
          return True
    return False
  
# complexidade de tempo: N + (N-1) + (N-2) + ... + 1 = N*(N-1)/2 
# (N^2 - N)/2 = O(N²)

    