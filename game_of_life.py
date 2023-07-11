import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from gui import GameOfLifeWidget


def perform_game_of_life(grid):
    """Performs one step of the Game of Life."""
    return grid


def init_grid(grid_size):
    """Initializes a grid with a few live cells."""
    new_grid = [[0] * grid_size for _ in range(grid_size)]
    new_grid[2][3] = 1
    new_grid[3][4] = 1
    new_grid[4][2] = 1
    new_grid[4][3] = 1
    new_grid[4][4] = 1
    return new_grid


def main():
    app = QApplication(sys.argv)

    grid_size = 20

    widget = QWidget()
    layout = QVBoxLayout(widget)
    layout.setContentsMargins(0, 0, 0, 0)

    game_of_life_widget = GameOfLifeWidget(grid_size)
    layout.addWidget(game_of_life_widget)

    grid = init_grid(grid_size)
    game_of_life_widget.update_grid(grid)
    widget.show()

    for _ in range(100):
        # Perform one step of the Game of Life and update the grid
        grid = perform_game_of_life(grid)
        game_of_life_widget.update_grid(grid)

        # Add a small delay to observe each step
        QApplication.processEvents()
        QApplication.processEvents()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
