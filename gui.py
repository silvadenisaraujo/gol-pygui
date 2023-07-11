from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFrame
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt


class GameOfLifeWidget(QFrame):
    def __init__(self, grid_size: int, cell_size: int = 20):
        super().__init__()

        self.grid_size = grid_size
        self.cell_size = cell_size
        self.grid = [[0] * grid_size for _ in range(grid_size)]

        self.setMinimumSize(grid_size * cell_size, grid_size * cell_size)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                x = j * self.cell_size
                y = i * self.cell_size

                if self.grid[i][j] == 1:
                    painter.setBrush(QColor(0, 0, 0))  # Black color for live cells
                else:
                    painter.setBrush(
                        QColor(255, 255, 255)
                    )  # White color for dead cells

                painter.drawRect(x, y, self.cell_size, self.cell_size)

    def update_grid(self, grid: list):
        self.grid = grid
        self.update()
