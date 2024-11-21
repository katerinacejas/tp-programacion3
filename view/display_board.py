import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

# Function to animate the Knight's Tour
def animate_knights_tour(N, moves):
    # Create the board
    board = np.full((N, N), -1, dtype=int)
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xticks(np.arange(-0.5, N, 1))
    ax.set_yticks(np.arange(-0.5, N, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(color='black', linestyle='-', linewidth=1)
    ax.set_xlim(-0.5, N - 0.5)
    ax.set_ylim(-0.5, N - 0.5)
    plt.gca().invert_yaxis()  # Invert Y-axis to match chessboard coordinates
    plt.title(f"Knight's Tour Animation on {N}x{N} Board", fontsize=16)

    # Draw the chessboard squares
    for x in range(N):
        for y in range(N):
            color = 'white' if (x + y) % 2 == 0 else 'gray'
            ax.add_patch(plt.Rectangle((y - 0.5, x - 0.5), 1, 1, color=color))

    # Plot elements
    step_text = ax.text(0, -1, "", fontsize=12, color="blue", ha="left")
    knight, = ax.plot([], [], 'ro', markersize=15)  # Knight's current position
    path_lines, = ax.plot([], [], 'r-', linewidth=1)  # Path lines

    # Initialize the animation path
    path_x, path_y = [], []

    def update(frame):
        nonlocal path_x, path_y

        # Get current move from the moves list
        start, end = moves[frame]

        # Update path lists
        path_x.append(start[1])
        path_y.append(start[0])
        path_x.append(end[1])
        path_y.append(end[0])

        # Update knight's position
        knight.set_data([end[1]], [end[0]])  # Ensure x, y are sequences

        # Update path lines (the red line tracking the knight)
        path_lines.set_data(path_x, path_y)

        # Update step count text
        step_text.set_text(f"Step {frame + 1}/{len(moves)}")

        # Return updated visual elements
        return knight, path_lines, step_text

    # Animation call
    ani = animation.FuncAnimation(
        fig,
        update,
        frames=len(moves),
        interval=500,
        blit=False,  # Disable blit for compatibility
        repeat=False
    )
    ani.save(f"knights_tour_size_{N}.gif")
    plt.show()