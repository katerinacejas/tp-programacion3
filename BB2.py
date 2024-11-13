import time

from Back8 import actualizarReturn


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

# Definimos el tamaño del tablero
N = 5  # Cambia este valor para tableros de diferentes tamaños

tablero=generar_tablero(N)

# Movimientos posibles del caballo
movimientos_x = [2, 1, -1, -2, -2, -1, 1, 2]
movimientos_y = [1, 2, 2, 1, -1, -2, -2, -1]

# Contador de pasos
total_pasos = 0

# Función para verificar si una posición (x, y) está dentro del tablero y no ha sido visitada
def es_movimiento_valido(x, y):
    return 0 <= x < N and 0 <= y < N and tablero[x][y] < 0

# Función para contar los movimientos posibles desde una posición (x, y)
def contar_movimientos_posibles(x, y):
    conteo = 0
    for i in range(8):
        nuevo_x = x + movimientos_x[i]
        nuevo_y = y + movimientos_y[i]
        if es_movimiento_valido(nuevo_x, nuevo_y):
            conteo += 1
    return conteo

def actualizar_return(x, y):
    if 0 <= x < N and 0 <= y < N:
        for a in range(8):
            nuevo_x_temp = x + movimientos_x[a]
            nuevo_y_temp = y + movimientos_y[a]
            if 0 <= nuevo_x_temp < N and 0 <= nuevo_y_temp < N and tablero[nuevo_x_temp][nuevo_y_temp] < 0:
                tablero[nuevo_x_temp][nuevo_y_temp] += 1

def devolver_valores(x, y):
    if 0 <= x < N and 0 <= y < N and tablero[x][y] > 0:
        for a in range(8):
            nuevo_x_temp = x + movimientos_x[a]
            nuevo_y_temp = y + movimientos_y[a]
            if 0 <= nuevo_x_temp < N and 0 <= nuevo_y_temp < N and tablero[nuevo_x_temp][nuevo_y_temp] <= 0 :
                tablero[nuevo_x_temp][nuevo_y_temp] -= 1
    #return False

# Función para imprimir el tablero celda por celda en el orden de recorrido
def imprimir_tablero_paso_a_paso():
    print("\nRecorrido final del tablero:")
    posiciones_ordenadas = sorted(
        [(i, j, tablero[i][j]) for i in range(N) for j in range(N)],
        key=lambda x: x[2]
    )
    for _, _, movimiento in posiciones_ordenadas:
        for i in range(N):
            for j in range(N):
                if tablero[i][j] <= movimiento and tablero[i][j] != -1:
                    print(f"{tablero[i][j]:2}", end=" ")
                else:
                    print(" . ", end=" ")
            print()
        print("\n" + "-" * (3 * N))
        time.sleep(0.2)


# Función recursiva de Branch & Bound con la heurística de Warnsdorff
def resolver_recorrido_caballo(x, y, movimiento):
    global total_pasos
    total_pasos += 1  # Incrementamos el contador de pasos

    if movimiento == N * N:
        return True

    # Generar todos los movimientos válidos desde (x, y) y ordenarlos usando la heurística
    movimientos_posibles = []
    for i in range(8):
        nuevo_x = x + movimientos_x[i]
        nuevo_y = y + movimientos_y[i]
        if es_movimiento_valido(nuevo_x, nuevo_y):
            # Contar los movimientos futuros posibles desde la nueva posición
            movimientos_posibles.append((contar_movimientos_posibles(nuevo_x, nuevo_y), nuevo_x, nuevo_y))

    # Ordenamos los movimientos posibles por el número de opciones futuras (heurística de Warnsdorff)
    movimientos_posibles.sort()  # Menor cantidad de opciones primero

    imprimir_tablero()
    # Intentar cada movimiento en el orden determinado por la heurística
    for _, nuevo_x, nuevo_y in movimientos_posibles:
        guardarPosicion = tablero[nuevo_x][nuevo_y]
        tablero[nuevo_x][nuevo_y] = movimiento  # Marcamos la posición con el número del movimiento
        actualizar_return(nuevo_x,nuevo_y)
        if resolver_recorrido_caballo(nuevo_x, nuevo_y, movimiento + 1):
            return True

        # Backtracking: desmarcar la casilla
        devolver_valores(nuevo_x,nuevo_y)
        tablero[nuevo_x][nuevo_y] = guardarPosicion

    return False

def imprimir_tablero():
    for fila in tablero:
        print(' '.join(f'{x:2}' for x in fila))
    print()

# Posición inicial del caballo (personalizable)
x_inicial, y_inicial = 2, 0  # Cambia estas coordenadas según sea necesario
tablero[x_inicial][y_inicial] = 1  # Marcamos la posición inicial

# Iniciar timers
start_time = time.time()

# Llamada a la función
if resolver_recorrido_caballo(x_inicial, y_inicial, 2):
    solution_time = time.time() - start_time  # Tiempo hasta encontrar la solución
    # imprimir_tablero_paso_a_paso()
    imprimir_tablero()
else:
    imprimir_tablero()
    print("No se encontró un recorrido válido.")

# Tiempo total de ejecución
total_time = time.time() - start_time
print(f"\nTiempo hasta encontrar la solución: {solution_time:.4f} segundos")
print(f"Tiempo total de ejecución: {total_time:.4f} segundos")
print(f"Total de pasos hasta encontrar la solución: {total_pasos}")
