import time

# Definimos el tamaño del tablero
N = 7  # Cambia este valor para tableros de diferentes tamaños

# Posición inicial del caballo
x_inicial, y_inicial = 0, 0 # Cambia estas coordenadas según sea necesario

# Movimientos posibles del caballo
movimientos_x = [2, 1, -1, -2, -2, -1, 1, 2]
movimientos_y = [1, 2, 2, 1, -1, -2, -2, -1]

# Variables de ejecución
total_pasos = 0

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

# Verificar si el movimiento es válido
def es_movimiento_valido(x, y):
    return 0 <= x < N and 0 <= y < N and tablero[x][y] < 0

def contar_ceros(tablero):
    ceros = sum(fila.count(0) for fila in tablero)
    return ceros > 1

def contar_movimientos_posibles(x, y, tablero):
    conteo = 0
    for i in range(8):
        nuevo_x = x + movimientos_x[i]
        nuevo_y = y + movimientos_y[i]
        if es_movimiento_valido(nuevo_x, nuevo_y):
            conteo += 1
    tablero[x][y] = tablero[x][y] + conteo

def actualizar_return(x, y):
    if 0 <= x < N and 0 <= y < N:
        for a in range(8):
            nuevo_x_temp = x + movimientos_x[a]
            nuevo_y_temp = y + movimientos_y[a]
            if 0 <= nuevo_x_temp < N and 0 <= nuevo_y_temp < N and tablero[nuevo_x_temp][nuevo_y_temp] < 0:
                tablero[nuevo_x_temp][nuevo_y_temp] += 1


# Función recursiva de Backtracking
def resolver_recorrido_caballo(x, y, movimiento, tablero):
    global total_pasos
    total_pasos += 1  # Incrementamos el contador de pasos

    # Si el caballo ha visitado todas las casillas, hemos terminado
    if movimiento == N * N:
        return True

    # Intentamos cada uno de los 8 posibles movimientos
    for i in range(8):
        nuevo_x = x + movimientos_x[i]
        nuevo_y = y + movimientos_y[i]

        if es_movimiento_valido(nuevo_x, nuevo_y):
            tablerotemp = [fila[:] for fila in tablero]
            tablero[nuevo_x][nuevo_y] = movimiento  # Marcamos la posición con el número del movimiento
            contar_movimientos_posibles(nuevo_x,nuevo_y,tablero)
            if(contar_ceros(tablero)):
                flag = flag + 1
                continue
            if resolver_recorrido_caballo(nuevo_x, nuevo_y, movimiento + 1, tablero):
                return True

            # Backtracking: desmarcar la casilla
            #tablero[nuevo_x][nuevo_y] = valorPrevio
            tablero = [fila[:] for fila in tablerotemp]

    return False

# Imprimir el tablero
def imprimir_tablero():
    for fila in tablero:
        print(' '.join(f'{x:2}' for x in fila))
    print()


# Configuración inicial
tablero = generar_tablero(N)
tablero[x_inicial][y_inicial] = 1

# Ejecución y medición de tiempo
start_time = time.time()
actualizar_return(x_inicial,y_inicial)

if resolver_recorrido_caballo(x_inicial, y_inicial, tablero[x_inicial][y_inicial] + 1, tablero):
    solution_time = time.time() - start_time
    print("Se encontró un recorrido válido.")
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
