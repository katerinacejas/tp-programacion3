import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import threading
import time

class KnightTourVisualizer:
    def __init__(self, N,knight_path):
        # Set up the plot
        self.board = np.zeros((N, N))
        self.fig, self.ax = plt.subplots()
        self.im = self.ax.imshow(self.board, cmap="Blues", vmin=0, vmax=1)
        self.ax.set_xticks(np.arange(N))
        self.ax.set_yticks(np.arange(N))
        
        ani = FuncAnimation(self.fig, self.update, frames=len(knight_path), interval=2000, blit=True)

    # Function to update the knight's position at each frame
    def update(self,frame):
        # Clear the board
        self.board.fill(0)
        # Update the knight's position
        x, y = knight_path[frame]
        self.board[x, y] = 1  # Mark the knight's current position
        self.im.set_array(self.board)
        self.ax.set_title(f"Move {frame + 1}: Position ({x}, {y})")
        return [self.im]

# Example usage
if __name__ == "__main__":
    board_size = 5  # Set the desired board size
    knight_path=[(0,0),(-1,-2),(0,-4)]
    knight_tour_visualizer = KnightTourVisualizer(board_size,knight_path)
    plt.show()
