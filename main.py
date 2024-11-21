import timeit
import csv

import pandas as pd

from Parte_1_Backtracking import KnightTourBacktracking
from view.display_board import KnightTourVisualizer

def displayBacktrackingSolution():
    board_size = 1
    backtracking = KnightTourBacktracking(board_size)
    if not backtracking.resolver_recorrido_caballo(0,0):
        print("No tiene solucion!")
        return
    print("Starting")
    KnightTourVisualizer(board_size,backtracking.get_recorrido()).show()

TEST_HEADERS = ["id","Algoritmo","N","X_inicial","Y_inicial","tiempoMS","existeSolucion","Nodos_Explorados","Camino_Encontrado"]
# # Ejemplo de uso
ID_GLOBAL = 0

def empezar_pruebas(algoritmo):
    global ID_GLOBAL

    if isinstance(algoritmo,KnightTourBacktracking):
        algoritmo_nombre = "Backtracking"
        with open(f"{algoritmo_nombre}_test_results.csv", 'w', newline='') as csvFile:
            csv_writer = csv.writer(csvFile, delimiter=',')
            csv_writer.writerow(TEST_HEADERS)

            for N in range(3, 7):
                algoritmo.setN(N)
                for x_inicial in range(N):
                    for y_inicial in range(N):
                        print(N, x_inicial, y_inicial)

                        try:
                            tiempo_ms = timeit.timeit(
                                lambda: algoritmo.resolver_recorrido_caballo(x_inicial, y_inicial), number=1)*1000
                        except Exception as e:
                            print(f"Error solving Knight's Tour: {e}")
                            continue

                        tiempo_execucion_formateado = f"{tiempo_ms:.4f}"
                        recorrido = algoritmo.get_recorrido()
                        cant_nodos_explorados = algoritmo.get_cant_nodos_explorados()
                        tiene_solucion = bool(recorrido)
                        row = [ID_GLOBAL, algoritmo_nombre, N, x_inicial, y_inicial, tiempo_execucion_formateado, tiene_solucion,
                               cant_nodos_explorados, recorrido]
                        print(row)
                        csv_writer.writerow(row)
                        ID_GLOBAL += 1
                    csvFile.flush()



if __name__ == "__main__":
    data = pd.read_csv("csv_results/Backtracking_test_results.csv", sep=",", header=0)
    print(data)
    empezar_pruebas(KnightTourBacktracking())
    # displayBacktrackingSolution()