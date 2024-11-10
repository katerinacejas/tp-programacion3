import time

# Definimos el tamaño del tablero
N = 8  # Cambia este valor para tableros de diferentes tamaños

# Movimientos posibles del caballo
movimientos_x = [2, 1, -1, -2, -2, -1, 1, 2]
movimientos_y = [1, 2, 2, 1, -1, -2, -2, -1]

# Inicializamos el tablero con -1 para marcar que ninguna posición ha sido visitada
tablero = [[-1 for _ in range(N)] for _ in range(N)]

# Contador de pasos
total_pasos = 0

# Función para verificar si una posición (x, y) está dentro del tablero y no ha sido visitada
def es_movimiento_valido(x, y):
    return 0 <= x < N and 0 <= y < N and tablero[x][y] == -1

# Función para imprimir el tablero celda por celda en el orden de recorrido
def imprimir_tablero_paso_a_paso():
    print("\nRecorrido final del tablero:")
    # Crear una lista de posiciones ordenadas por el número de movimiento
    posiciones_ordenadas = sorted(
        [(i, j, tablero[i][j]) for i in range(N) for j in range(N)],
        key=lambda x: x[2]
    )
    # Imprimir cada movimiento en su posición final
    for _, _, movimiento in posiciones_ordenadas:
        for i in range(N):
            fila = ""
            for j in range(N):
                # Mostrar la celda con el movimiento actual o un punto si aún no se ha alcanzado ese movimiento
                if tablero[i][j] <= movimiento:
                    fila += f"{tablero[i][j]:2} "
                else:
                    fila += " . "
            print(fila)
        print("\n" + "-" * (3 * N))  # Separador entre estados del tablero
        time.sleep(0.5)  # Espera para ver el movimiento uno por uno

# Función recursiva de Backtracking
def resolver_recorrido_caballo(x, y, movimiento):
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
            tablero[nuevo_x][nuevo_y] = movimiento  # Marcamos la posición con el número del movimiento

            if resolver_recorrido_caballo(nuevo_x, nuevo_y, movimiento + 1):
                return True

            # Backtracking: desmarcar la casilla
            tablero[nuevo_x][nuevo_y] = -1

    return False

# Posición inicial del caballo (personalizable)
x_inicial, y_inicial = 1, 1  # Cambia estas coordenadas según sea necesario
tablero[x_inicial][y_inicial] = 0  # Marcamos la posición inicial

# Iniciar timers
start_time = time.time()

# Llamada a la función
if resolver_recorrido_caballo(x_inicial, y_inicial, 1):
    solution_time = time.time() - start_time  # Tiempo hasta encontrar la solución
    imprimir_tablero_paso_a_paso()
else:
    solution_time = time.time() - start_time  # Tiempo hasta encontrar la solución
    print("No se encontró un recorrido válido.")

# Tiempo total de ejecución
total_time = time.time() - start_time
print(f"\nTiempo hasta encontrar la solución: {solution_time:.4f} segundos")
print(f"Tiempo total de ejecución: {total_time:.4f} segundos")
print(f"Total de pasos hasta encontrar la solución: {total_pasos}")
