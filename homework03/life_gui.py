import pygame
from life import GameOfLife
from pygame.locals import *
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)
        self.cell_size = cell_size
        self.speed = speed

        # Вычисляем количество пикселей по вертикали и горизонтали
        self.width = life.cols * cell_size
        self.height = life.rows * cell_size

        # Устанавливаем размер окна
        self.screen_size = self.width, self.height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def draw_grid(self) -> None:
        for y in range(1, self.height, self.cell_size):
            for x in range(1, self.width, self.cell_size):
                if self.life.curr_generation[y // self.cell_size][x // self.cell_size] == 0:
                    pygame.draw.rect(
                        self.screen,
                        pygame.Color("white"),
                        (x, y, self.cell_size - 1, self.cell_size - 1),
                    )
                else:
                    pygame.draw.rect(
                        self.screen,
                        pygame.Color("green"),
                        (x, y, self.cell_size - 1, self.cell_size - 1),
                    )

    def run(self) -> None:
        """Запустить игру"""
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        # Создание списка клеток
        self.life.create_grid(True)

        running = True
        paused = False
        while running and self.life.is_changing and not self.life.is_max_generations_exceeded:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    paused = not paused

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = [coord // self.cell_size for coord in event.pos]
                    if self.life.curr_generation[y][x] == 0:
                        self.life.curr_generation[y][x] = 1
                    else:
                        self.life.curr_generation[y][x] = 0

            self.draw_lines()

            # Отрисовка списка клеток
            # Выполнение одного шага игры (обновление состояния ячеек)
            self.draw_grid()

            if not paused:
                self.life.step()

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()


if __name__ == "__main__":
    life = GameOfLife((30, 40), max_generations=100)
    gui = GUI(life, 20)
    gui.run()
