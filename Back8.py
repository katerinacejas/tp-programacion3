import time
from operator import truediv

# Función para generar el tablero con los posibles movimientos
def generar_tablero(N):
    # Inicializamos el tablero vacío como una lista de listas
    tablero = [[0] * N for _ in range(N)]

    # Determinar el número de capas
    capas = (N + 1) // 2  # Se determina la cantidad de capas

    # Asignamos los valores a cada capa
    for capa in range(capas):
        # Calculamos los valores de la capa
        if capa == 0:
            # Capa más externa
            valor_vertice = -2
            valor_adyacente = -3
            valor_interno = -4
        elif capa == 1:
            # Segunda capa
            valor_vertice = -4
            valor_adyacente = -6
            valor_interno = -6
        else:
            # Capas internas
            valor_vertice = -8
            valor_adyacente = -8
            valor_interno = -8

        # Coordenadas del borde de la capa (el cuadrado de la capa)
        min_coord = capa
        max_coord = N - capa - 1

        # Asignamos los valores a las posiciones de la capa
        for i in range(min_coord, max_coord + 1):
            for j in range(min_coord, max_coord + 1):
                # Para la capa más externa, tratamos los vértices por separado
                if capa == 0:
                    if (i == min_coord and j == min_coord) or (i == min_coord and j == max_coord) or (i == max_coord and j == min_coord) or (i == max_coord and j == max_coord):
                        # Asignamos valor 2 a los vértices
                        tablero[i][j] = valor_vertice
                    elif (i == min_coord and j == min_coord+1) or (i == min_coord and j == max_coord-1) or (i == max_coord-1 and j == min_coord) or (i == max_coord and j == max_coord-1) or (i == min_coord+1 and j == min_coord) or (i == min_coord+1 and j == max_coord) or (i == max_coord and j == min_coord+1) or (i == max_coord-1 and j == max_coord):
                        # Asignamos valor 3 a las celdas adyacentes a los vértices
                        tablero[i][j] = valor_adyacente
                    else:
                        # Asignamos valor 4 al resto de las celdas
                        tablero[i][j] = valor_interno
                else:
                    # Para las demás capas
                    if (i == min_coord or i == max_coord) and (j == min_coord or j == max_coord):
                        # Asignamos valor 4 a los vértices
                        tablero[i][j] = valor_vertice
                    elif (i == min_coord or i == max_coord) or (j == min_coord or j == max_coord):
                        # Asignamos valor 6 a las celdas adyacentes a los vértices
                        tablero[i][j] = valor_adyacente
                    else:
                        # Asignamos valor 6 al resto de las celdas
                        tablero[i][j] = valor_interno

    return tablero

# Definimos el tamaño del tablero
N = 5  # Cambia este valor para tableros de diferentes tamaños

# Movimientos posibles del caballo
movimientos_x = [2, 1, -1, -2, -2, -1, 1, 2]
movimientos_y = [1, 2, 2, 1, -1, -2, -2, -1]

# Inicializamos el tablero con los valores generados
tablero = generar_tablero(N)

# Contador de pasos
total_pasos = 0

# Función para verificar si una posición (x, y) está dentro del tablero y no ha sido visitada
def es_movimiento_valido(x, y):
    if(0 <= x < N and 0 <= y < N and tablero[x][y] < 0):
        for a in range(8):
            nuevo_x_temp = x + movimientos_x[a]
            nuevo_y_temp = y + movimientos_y[a]
            if(0 <= nuevo_x_temp < N and 0 <= nuevo_y_temp < N and tablero[nuevo_x_temp][nuevo_y_temp] < 0):
                tablero[nuevo_x_temp][nuevo_y_temp] = tablero[nuevo_x_temp][nuevo_y_temp] + 1
                if(tablero[nuevo_x_temp][nuevo_y_temp]==0):
                    for b in range(a+1):
                        nuevo_x_temp2 = x + movimientos_x[b]
                        nuevo_y_temp2 = y + movimientos_y[b]
                        if(0 <= nuevo_x_temp2 < N and 0 <= nuevo_y_temp2 < N and tablero[nuevo_x_temp2][nuevo_y_temp2] <= 0):
                            tablero[nuevo_x_temp2][nuevo_y_temp2] = tablero[nuevo_x_temp2][nuevo_y_temp2] - 1
                    return False
        return True
    else:
        return False
    #return 0 <= x < N and 0 <= y < N and tablero[x][y] < 0

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
#        time.sleep(0.5)  # Espera para ver el movimiento uno por uno

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
            valorPrevio = tablero[nuevo_x][nuevo_y]
            tablero[nuevo_x][nuevo_y] = movimiento  # Marcamos la posición con el número del movimiento
            if resolver_recorrido_caballo(nuevo_x, nuevo_y, movimiento + 1):
                return True
            if movimiento == N * N:
                return True
            tablero[nuevo_x][nuevo_y] = valorPrevio
    return False

def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(f'{x:2}' for x in fila))
    print()

def imprimir_tablero_entero():
    print("\nRecorrido final del tablero:")
    for i in range(N):
        fila = ""
        for j in range(N):
            # Mostrar la celda con el número del movimiento o un punto si no se ha visitado
            if tablero[i][j] != -1:
                fila += f"{tablero[i][j]:2} "  # Muestra el número de movimiento
            else:
                fila += " . "  # Punto para celdas no visitadas
        print(fila)
    print("\n" + "-" * (3 * N))  # Separador entre estados del tablero

# Posición inicial del caballo (personalizable)
x_inicial, y_inicial = 0, 0  # Cambia estas coordenadas según sea necesario
tablero[x_inicial][y_inicial] = 1  # Marcamos la posición inicial

# Iniciar timers
start_time = time.time()

imprimir_tablero(tablero)

# Llamada a la función
if resolver_recorrido_caballo(x_inicial, y_inicial, 2):
    solution_time = time.time() - start_time  # Tiempo hasta encontrar la solución
    imprimir_tablero(tablero)
else:
    solution_time = time.time() - start_time  # Tiempo hasta encontrar la solución
    print("No se encontró un recorrido válido.")

# Tiempo total de ejecución
total_time = time.time() - start_time
print(f"\nTiempo hasta encontrar la solución: {solution_time:.4f} segundos")
print(f"Tiempo total de ejecución: {total_time:.4f} segundos")
print(f"Total de pasos hasta encontrar la solución: {total_pasos}")
