import time

# Definimos el tamaño del tablero
N = 8  # Cambia este valor para tableros de diferentes tamaños

# Posición inicial del caballo
x_inicial, y_inicial = 2, 0  # Cambia estas coordenadas según sea necesario

# Movimientos posibles del caballo
movimientos_x = [2, 1, -1, -2, -2, -1, 1, 2]
movimientos_y = [1, 2, 2, 1, -1, -2, -2, -1]

# Contador de pasos
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

def contar_ceros(tablero):
    ceros = sum(fila.count(0) for fila in tablero)
    return ceros > 0

def contar_movimientos_posibles(x, y):
    conteo = 0
    for i in range(8):
        nuevo_x = x + movimientos_x[i]
        nuevo_y = y + movimientos_y[i]
        if es_movimiento_valido(nuevo_x, nuevo_y):
            conteo += 1
    return conteo

# Verificar si el movimiento es válido
def es_movimiento_valido(x, y):
    return 0 <= x < N and 0 <= y < N and tablero[x][y] < 0

def actualizar_return(x, y):
    if 0 <= x < N and 0 <= y < N and tablero[x][y] < 0:
        for a in range(8):
            nuevo_x_temp = x + movimientos_x[a]
            nuevo_y_temp = y + movimientos_y[a]
            if 0 <= nuevo_x_temp < N and 0 <= nuevo_y_temp < N and tablero[nuevo_x_temp][nuevo_y_temp] < 0:
                tablero[nuevo_x_temp][nuevo_y_temp] += 1

# Función recursiva de Backtracking
def resolver_recorrido_caballo(x, y, movimiento):
    global total_pasos, tablero
    total_pasos += 1
    if movimiento == (N * N)+1:
        print("Salio por acá.")
        return True

    # Generar todos los movimientos válidos desde (x, y) y ordenarlos usando la heurística
    movimientos_posibles = []
    for i in range(8):
        nuevo_x = x + movimientos_x[i]
        nuevo_y = y + movimientos_y[i]
        if es_movimiento_valido(nuevo_x, nuevo_y):
            movimientos_posibles.append((contar_movimientos_posibles(nuevo_x, nuevo_y), nuevo_x, nuevo_y))

    # Ordenamos los movimientos posibles por el número de opciones futuras (heurística de Warnsdorff)
    movimientos_posibles.sort()  # Menor cantidad de opciones primero
    # Intentar cada movimiento en el orden determinado por la heurística
    for _, nuevo_x, nuevo_y in movimientos_posibles:
        recorrido.append([(x, y), (nuevo_x, nuevo_y)])
        tablerotemp = [fila[:] for fila in tablero]
        tablero[nuevo_x][nuevo_y] = movimiento  # Marcamos la posición con el número del movimiento
        actualizar_return(nuevo_x,nuevo_y)
        if(contar_ceros(tablero)):
            tablero = [fila[:] for fila in tablerotemp]
            recorrido.pop()
            continue
        if resolver_recorrido_caballo(nuevo_x, nuevo_y, movimiento + 1):
            return True

        # Backtracking: desmarcar la casilla
        #tablero = [fila[:] for fila in tablerotemp]
    return False

# Imprimir el tablero
def imprimir_tablero():
    for fila in tablero:
        print(' '.join(f'{x:2}' for x in fila))
    print()


# Configuración inicial
tablero = generar_tablero(N)
tablero[x_inicial][y_inicial] = 1
recorrido = []

actualizar_return(x_inicial,y_inicial)
# Ejecución y medición de tiempo
start_time = time.time()
imprimir_tablero()

if resolver_recorrido_caballo(x_inicial, y_inicial, tablero[x_inicial][y_inicial] + 1):
    solution_time = time.time() - start_time
    print("Se encontró un recorrido válido.")
    imprimir_tablero()
    print(f"Este es el recorrido: {recorrido}" )
else:
    solution_time = time.time() - start_time
    imprimir_tablero()
    print("No se encontró un recorrido válido.")

# Resultados de tiempo
total_time = time.time() - start_time
print(f"\nTiempo hasta encontrar la solución: {solution_time:.4f} segundos")
print(f"Tiempo total de ejecución: {total_time:.4f} segundos")
print(f"Total de pasos hasta encontrar la solución: {total_pasos}")
