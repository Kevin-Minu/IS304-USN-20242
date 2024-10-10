import random
import time

# Algoritmos de ordenamiento

# Bubble Sort
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

# Selection Sort
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

# Insertion Sort
def insertion_sort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key

# Merge Sort
def merge_sort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        izquierda = lista[:mid]
        derecha = lista[mid:]

        # Ordenar las dos mitades
        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0

        # Combinar las dos mitades
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        # Chequear si quedan elementos
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

# Función para medir tiempo de ejecución
def medir_tiempo(algoritmo, lista):
    inicio = time.time()  # Capturamos el tiempo inicial
    algoritmo(lista)  # Ejecutamos el algoritmo de ordenamiento
    fin = time.time()  # Capturamos el tiempo final
    return fin - inicio  # Retornamos el tiempo transcurrido

# Programa principal
if __name__ == "__main__":
    # Generamos una lista de 10,000 valores aleatorios
    lista_original = [random.randint(1, 10000) for _ in range(10000)]

    # Diccionario para guardar los tiempos de cada método
    tiempos = {}

    # Ejecutamos cada algoritmo y medimos el tiempo
    for metodo in [("Bubble Sort", bubble_sort), 
                   ("Selection Sort", selection_sort), 
                   ("Insertion Sort", insertion_sort), 
                   ("Merge Sort", merge_sort)]:
        nombre, funcion = metodo
        lista_para_ordenar = lista_original.copy()  # Copiamos la lista original para no modificarla
        tiempo = medir_tiempo(funcion, lista_para_ordenar)  # Medimos el tiempo de ejecución
        tiempos[nombre] = tiempo

    # Ordenamos los métodos por tiempo de ejecución (de menor a mayor)
    tiempos_ordenados = sorted(tiempos.items(), key=lambda x: x[1])

    # Imprimimos los resultados
    print("Tiempos de ordenamiento (de menor a mayor):")
    for nombre, tiempo in tiempos_ordenados:
        print(f"{nombre}: {tiempo:.6f} segundos")
