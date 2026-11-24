""""Predice la salida y explica por qué pasa. Después, escribe la versión correcta."""

matriz = [[0] * 2] * 2
matriz[0][0] = 1
print(matriz)

matriz = [[0] * 2 for _ in range(2)]
matriz[0][0] = 1
print(matriz)      # [[1, 0], [0, 0]]