import pathlib
import random
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:

        grid = [[0] * self.cols] * self.rows
        if randomize:
            grid = [[random.choice([0, 1]) for i in row] for row in grid]
        return grid

    def get_neighbours(self, cell: Cell) -> Cells:

        y, x = cell[0], cell[1]
        neighbours = [
            (y - 1, x - 1),
            (y - 1, x),
            (y - 1, x + 1),
            (y, x + 1),
            (y + 1, x + 1),
            (y + 1, x),
            (y + 1, x - 1),
            (y, x - 1),
        ]
        cells = []
        for coord in neighbours:
            a, b = coord
            if 0 <= a < self.rows and 0 <= b < self.cols:
                cells.append(self.curr_generation[a][b])
        return cells

    def get_next_generation(self) -> Grid:

        grid = [[i for i in row] for row in self.curr_generation]
        for y in range(self.rows):
            for x in range(self.cols):
                c = self.curr_generation[y][x]
                n = sum(self.get_neighbours((y, x)))
                if c == 1 and not 2 <= n <= 3:
                    grid[y][x] = 0
                elif c == 0 and n == 3:
                    grid[y][x] = 1

        return grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = self.curr_generation
        self.curr_generation = self.get_next_generation()
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        if self.max_generations and self.generations >= self.max_generations:
            return True
        return False

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        if self.curr_generation == self.prev_generation:
            return False
        return True

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        grid = []
        with open(filename) as f:
            for line in f:
                row = [int(i) for i in line.strip()]
                if row:
                    grid.append(row)
                    cols = len(row)
        game = GameOfLife((len(grid), cols))
        game.curr_generation = grid
        return game

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        with open(filename, "w") as f:
            for i in self.curr_generation:
                for j in i:
                    f.write(str(j))
                f.write("\n")
