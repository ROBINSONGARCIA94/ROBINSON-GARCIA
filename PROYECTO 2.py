def ordenar_fila(matriz, fila):
    # Obtener la fila específica
    fila_ordenar = matriz[fila]

    # Ordenar la fila usando el método sort
    fila_ordenar.sort()


def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)


def main():
    # Definir una matriz de ejemplo
    matriz = [
        [3, 1, 4],
        [1, 5, 9],
        [2, 6, 5]
    ]

    print("Matriz original:")
    imprimir_matriz(matriz)

    fila_a_ordenar = 1  # Indica la fila que quieres ordenar (0-indexado)
    ordenar_fila(matriz, fila_a_ordenar)

    print("\nMatriz con la fila ordenada:")
    imprimir_matriz(matriz)


if __name__ == "__main__":
    main()
