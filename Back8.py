import time

# Función para generar el tablero con los valores específicos
def generar_tablero(N):
    tablero = [[0] * N for _ in range(N)]
    capas = (N + 1) // 2  # Cantidad de capas

    # Asignación de valores a cada capa
    for capa in range(capas):
        if capa == 0:
            valor_vertice = -2
            valor_adyacente = -3
            valor_interno = -4
        elif capa == 1:
            valor_vertice = -4
            valor_adyacente = -6
            valor_interno = -6
        else:
            valor_vertice = -8
            valor_adyacente = -8
            valor_interno = -8

        min_coord = capa
        max_coord = N - capa - 1

        for i in range(min_coord, max_coord + 1):
            for j in range(min_coord, max_coord + 1):
                if capa == 0:
                    if (i == min_coord and j == min_coord) or (i == min_coord and j == max_coord) or \
                            (i == max_coord and j == min_coord) or (i == max_coord and j == max_coord):
                        tablero[i][j] = valor_vertice
                    elif (i == min_coord+1 and j in [min_coord, max_coord]) or \
                            (i == max_coord-1 and j in [min_coord, max_coord]) or \
                            (j == min_coord+1 and i in [min_coord, max_coord]) or \
                            (j == max_coord-1 and i in [min_coord, max_coord]):
                        tablero[i][j] = valor_adyacente
                    else:
                        tablero[i][j] = valor_interno
                else:
                    if (i == min_coord or i == max_coord) and (j == min_coord or j == max_coord):
                        tablero[i][j] = valor_vertice
                    elif (i == min_coord or i == max_coord) or (j == min_coord or j == max_coord):
                        tablero[i][j] = valor_adyacente
                    else:
                        tablero[i][j] = valor_interno
    return tablero

# Movimientos posibles del caballo
movimientos_x = [2, 1, -1, -2, -2, -1, 1, 2]
movimientos_y = [1, 2, 2, 1, -1, -2, -2, -1]

# Variables de ejecución
total_pasos = 0
contador = 0
N = 7  # Tamaño del tablero

# Verificar si el movimiento es válido
def es_movimiento_valido(x, y):
    return 0 <= x < N and 0 <= y < N and tablero[x][y] < 0

# Función recursiva de Backtracking
def resolver_recorrido_caballo(x, y, movimiento):
    global total_pasos
    total_pasos += 1
    if movimiento == (N * N)+1:
        return True

    for i in range(8):
        nuevo_x = x + movimientos_x[i]
        nuevo_y = y + movimientos_y[i]
        if es_movimiento_valido(nuevo_x, nuevo_y):
            valorPrevio = tablero[nuevo_x][nuevo_y]
            tablero[nuevo_x][nuevo_y] = movimiento
            if resolver_recorrido_caballo(nuevo_x, nuevo_y, movimiento + 1):
                return True
            actualizarReturn(nuevo_x,nuevo_y)
            tablero[nuevo_x][nuevo_y] = valorPrevio
    return False

# Imprimir el tablero
def imprimir_tablero():
    for fila in tablero:
        print(' '.join(f'{x:2}' for x in fila))
    print()


def actualizarReturn(x, y):
    if 0 <= x < N and 0 <= y < N and tablero[x][y] < 0:
        for a in range(8):
            nuevo_x_temp = x + movimientos_x[a]
            nuevo_y_temp = y + movimientos_y[a]
            if 0 <= nuevo_x_temp < N and 0 <= nuevo_y_temp < N and tablero[nuevo_x_temp][nuevo_y_temp] <= 0 :
                tablero[nuevo_x_temp][nuevo_y_temp] -= 1

def actualizar1erPosicionReturn(x, y):
    if 0 <= x < N and 0 <= y < N:
        for a in range(8):
            nuevo_x_temp = x + movimientos_x[a]
            nuevo_y_temp = y + movimientos_y[a]
            if 0 <= nuevo_x_temp < N and 0 <= nuevo_y_temp < N and tablero[nuevo_x_temp][nuevo_y_temp] < 0:
                tablero[nuevo_x_temp][nuevo_y_temp] += 1

# Configuración inicial
tablero = generar_tablero(N)
x_inicial, y_inicial = 0, 0
tablero[x_inicial][y_inicial] = 1

actualizar1erPosicionReturn(x_inicial,y_inicial)
# Ejecución y medición de tiempo
start_time = time.time()
imprimir_tablero()

if resolver_recorrido_caballo(x_inicial, y_inicial, tablero[x_inicial][y_inicial] + 1):
    solution_time = time.time() - start_time
    imprimir_tablero()
else:
    solution_time = time.time() - start_time
    imprimir_tablero()
    print("No se encontró un recorrido válido.")

# Resultados de tiempo
total_time = time.time() - start_time
print(f"\nTiempo hasta encontrar la solución: {solution_time:.4f} segundos")
print(f"Tiempo total de ejecución: {total_time:.4f} segundos")
print(f"Total de pasos hasta encontrar la solución: {total_pasos}")
