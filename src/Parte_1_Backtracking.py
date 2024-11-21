import time
from enum import Enum

from zmq.backend.cython import monitored_queue


class KnightTourBacktracking:
    movimientos_x = [2, 1, -1, -2, -2, -1, 1, 2]
    movimientos_y = [1, 2, 2, 1, -1, -2, -2, -1]
    tablero = []
    recorrido = []
    recorridos = []
    nodos_explorados = 0
    total_pasos = 0
    x_inicial = 0
    y_inicial = 0

    def __init__(self, n = 3):
        self.MAX_MULTIPLES_SOLUCIONES = 5
        self.N = n
        self.init_tablero()

    def init_tablero(self):
        self.tablero = [[-1 for _ in range(self.N)] for _ in range(self.N)]

    # Función para verificar si una posición (x, y) está dentro del tablero y no ha sido visitada    
    def es_movimiento_valido(self,x, y):
        x_valido = 0 <= x < self.N
        y_valido = 0 <= y < self.N
        celda_no_visitada = False
        if x_valido and y_valido:
            celda_no_visitada = self.tablero[x][y] == -1
        return x_valido and y_valido and celda_no_visitada

    def get_recorrido(self):
        return self.recorrido

    def instanciar(self,x_inicial,y_inicial):
        self.init_tablero()
        self.nodos_explorados = 0
        self.x_inicial = x_inicial
        self.y_inicial = y_inicial
        self.recorrido = []
        self.recorridos = []
        self.tablero[x_inicial][y_inicial] = 0

    # Función recursiva de Backtracking
    def resolver_recorrido_caballo(self,x_inicial, y_inicial,movimiento=0):
        if movimiento == 0:
            self.instanciar(x_inicial,y_inicial)
            movimiento += 1

        # Si el caballo ha visitado todas las casillas, hemos terminado
        if  movimiento == self.N * self.N:
            return True

        # Intentamos cada uno de los 8 posibles movimientos
        for i in range(8):
            nuevo_x = x_inicial + self.movimientos_x[i]
            nuevo_y = y_inicial + self.movimientos_y[i]

            if self.es_movimiento_valido(nuevo_x, nuevo_y):
                self.nodos_explorados += 1
                self.tablero[nuevo_x][nuevo_y] = movimiento # Marcamos la posición con el número del movimiento

                self.recorrido.append(((x_inicial, y_inicial), (nuevo_x, nuevo_y)))
                if self.resolver_recorrido_caballo(nuevo_x, nuevo_y, movimiento + 1):
                    return True

                # Backtracking: desmarcar la casilla
                self.tablero[nuevo_x][nuevo_y] = -1
                self.recorrido.pop()
        return False

    def imprimir_tablero(self):
        for fila in self.tablero:
            print(' '.join(f'{x:2}' for x in fila))
        print()
    #
    def resolver_varios_caminos_caballo(self,x_inicial, y_inicial,movimiento=0,cant_soluciones=3):
        if cant_soluciones > 5 :
            raise ValueError("Ingrese maximo de 5 cant_soluciones ")

        if movimiento == 0:
            self.instanciar(x_inicial, y_inicial)
            movimiento += 1

        self.total_pasos += 1  # Incrementamos el contador de pasos

        # Si el caballo ha visitado todas las casillas, hemos terminado
        if movimiento == self.N * self.N:
            self.recorridos.append(self.recorrido)
            if len(self.recorridos) == cant_soluciones:
                return True
            return False
        # Intentamos cada uno de los 8 posibles movimientos
        for i in range(8):
            nuevo_x = x_inicial + self.movimientos_x[i]
            nuevo_y = y_inicial + self.movimientos_y[i]

            if self.es_movimiento_valido(nuevo_x, nuevo_y):
                self.tablero[nuevo_x][nuevo_y] = movimiento  # Marcamos la posición con el número del movimiento
                self.recorrido.append(((x_inicial, y_inicial), (nuevo_x, nuevo_y)))
                if self.resolver_varios_caminos_caballo(nuevo_x, nuevo_y, movimiento + 1,cant_soluciones):
                    return True

                self.tablero[nuevo_x][nuevo_y] = -1
                self.recorrido.pop()
        return False

    def get_cant_nodos_explorados(self) -> int:
        return self.nodos_explorados

    def setN(self, N):
        if N < 3:
            raise ValueError('Size of board needs to be greater than N = 3.')
        self.N = N

    def get_caminos(self):
        return self.recorridos


