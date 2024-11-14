import time

# Definimos el tamaño del tablero
N = 7  # Cambia este valor para tableros de diferentes tamaños

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
            recorrido.append([(x, y), (nuevo_x, nuevo_y)])
            if resolver_recorrido_caballo(nuevo_x, nuevo_y, movimiento + 1):
                return True

            # Backtracking: desmarcar la casilla
            tablero[nuevo_x][nuevo_y] = -1
            recorrido.pop()
    return False

def imprimir_tablero():
    for fila in tablero:
        print(' '.join(f'{x:2}' for x in fila))
    print()

# Inicializamos el tablero con -1 para marcar que ninguna posición ha sido visitada
tablero = [[-1 for _ in range(N)] for _ in range(N)]
tablero[x_inicial][y_inicial] = 0  # Marcamos la posición inicial
recorrido = []

# Iniciar timers
start_time = time.time()

# Llamada a la función
if resolver_recorrido_caballo(x_inicial, y_inicial, 1):
    solution_time = time.time() - start_time  # Tiempo hasta encontrar la solución
    print("Se encontró un recorrido válido.")
    imprimir_tablero()
    print(f"Este es el recorrido: {recorrido}" )
else:
    solution_time = time.time() - start_time  # Tiempo hasta encontrar la solución
    print("No se encontró un recorrido válido.")

# Tiempo total de ejecución
total_time = time.time() - start_time
print(f"\nTiempo hasta encontrar la solución: {solution_time:.4f} segundos")
print(f"Tiempo total de ejecución: {total_time:.4f} segundos")
print(f"Total de pasos hasta encontrar la solución: {total_pasos}")
