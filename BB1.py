import time

# Definimos el tamaño del tablero
N = 10  # Cambia este valor para tableros de diferentes tamaños

# Posición inicial del caballo
x_inicial, y_inicial = 0, 0  # Cambia estas coordenadas según sea necesario

# Movimientos posibles del caballo
movimientos_x = [2, 1, -1, -2, -2, -1, 1, 2]
movimientos_y = [1, 2, 2, 1, -1, -2, -2, -1]

# Contador de pasos
total_pasos = 0

# Función para verificar si una posición (x, y) está dentro del tablero y no ha sido visitada
def es_movimiento_valido(x, y):
    return 0 <= x < N and 0 <= y < N and tablero[x][y] == -1

# Función para contar los movimientos posibles desde una posición (x, y)
def contar_movimientos_posibles(x, y):
    conteo = 0
    for i in range(8):
        nuevo_x = x + movimientos_x[i]
        nuevo_y = y + movimientos_y[i]
        if es_movimiento_valido(nuevo_x, nuevo_y):
            conteo += 1
    return conteo

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
        print("Salio por acá.")
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
    # Intentar cada movimiento en el orden determinado por la heurística
    for _, nuevo_x, nuevo_y in movimientos_posibles:
        tablero[nuevo_x][nuevo_y] = movimiento  # Marcamos la posición con el número del movimiento

        if resolver_recorrido_caballo(nuevo_x, nuevo_y, movimiento + 1):
            return True

        # Backtracking: desmarcar la casilla
        tablero[nuevo_x][nuevo_y] = -1

    return False

def imprimir_tablero():
    for fila in tablero:
        print(' '.join(f'{x:2}' for x in fila))
    print()

# Inicializamos el tablero con -1 para marcar que ninguna posición ha sido visitada
tablero = [[-1 for _ in range(N)] for _ in range(N)]
tablero[x_inicial][y_inicial] = 0  # Marcamos la posición inicial

# Iniciar timers
start_time = time.time()

# Llamada a la función
if resolver_recorrido_caballo(x_inicial, y_inicial, 1):
    solution_time = time.time() - start_time  # Tiempo hasta encontrar la solución
    print("Se encontró un recorrido válido.")
    imprimir_tablero()
else:
    imprimir_tablero()
    print("No se encontró un recorrido válido.")

# Tiempo total de ejecución
total_time = time.time() - start_time
print(f"\nTiempo hasta encontrar la solución: {solution_time:.4f} segundos")
print(f"Tiempo total de ejecución: {total_time:.4f} segundos")
print(f"Total de pasos hasta encontrar la solución: {total_pasos}")
