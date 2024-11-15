import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.colors import Colormap


class KnightTourVisualizer:
    def __init__(self, board_size, knight_path):
        self.knight_path = knight_path  # Guardar knight_path como atributo
        self.board_size = board_size
        self._setup_board()

    def _setup_board(self):
        # Configurar el tablero
        self.board = np.zeros([self.board_size, self.board_size], dtype=int)
        self.fig, self.axis = plt.subplots()

        self.axis.matshow(self.board,vmin=0,vmax=len(self.knight_path), cmap="Greys")

        # Asignar algunos valores de ejemplo


        self._setup_board_text()

    def _setup_board_text(self):
        for i in range(len(self.knight_path)):
            self.board[self.knight_path[i]] = i + 1
            for j in range(len(self.board)):
                self.axis.text(i, j, str(self.board[i, j]), ha="center", va="center")
                print(self.board[i, j])  # Este print puede ser removido si no es necesario

# Uso del código
# knight_tour_visualizer = KnightTourVisualizer(8, [(0, 0), (1, 2), (2, 0)])
# knight_tour_visualizer.show()

    #
    # # Función para configurar la animación
    # def setup_plot(self):
    #     self.board.fill(0)  # Limpiar el tablero inicial
    #     self.im.set_array(self.board)
    #     return [self.im]
    #
    # # Función para actualizar la posición del caballo en cada fotograma
    # def update(self, frame):
    #     x, y = self.knight_path[frame]  # Actualizar la posición del caballo
    #
    #     if 0 <= x < self.board_size and 0 <= y < self.board_size:
    #         self.board[x, y] = frame + 1# Marcar la posición actual del caballo
    #         self.im.set_array(self.board)
    #         self.axis.set_title(f"Move {frame + 1}: Position ({x}, {y})")
    #
    #     return [self.im]

    def show(self):
        # animation = FuncAnimation(fig=self.fig,
        #                           func=self.update,
        #                           frames=len(self.knight_path),
        #                           interval=100000,
        #                           )
        # animation.save("animation.gif")
        plt.show()


# # Ejemplo de uso
# if __name__ == "__main__":
#     board_size = 5  # Tamaño del tablero
#     x_inicial = 0
#     y_inicial = 0
#
#     knight_tour_visualizer = KnightTourVisualizer(board_size,recorrido)
#     knight_tour_visualizer.show()