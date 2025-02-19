import pygame
import numpy as np
from . import BaseGrid


class SquareGrid(BaseGrid):

    def set_up_window(self) -> None:
        height, width = len(self.automaton.grid), len(self.automaton.grid[0])
        self.screen: pygame.Surface = pygame.Surface((width, height))
        self.window: pygame.Surface = pygame.display.set_mode(size=(width * self.tile_size, height * self.tile_size))

        # Pre-compute color array for faster lookup
        self.color_array = []
        for color in self.colors:
            if isinstance(color, str):
                c = pygame.Color(color)
                color = (c.r, c.g, c.b)
            self.color_array.append(color)

        self.color_array = np.array(self.color_array)

    def draw_grid(self) -> None:
        # Convert grid to color indices
        grid = np.asarray(self.automaton.grid)

        # Create RGB array from the grid
        height, width = grid.shape
        rgb_array = np.zeros((width, height, 3), dtype=np.uint8)  # Note: width, height order for pygame

        for i, color in enumerate(self.color_array):
            mask = (grid.T == i)  # Transpose the grid to match pygame's format
            rgb_array[mask] = color

        # Blit the array to screen
        pygame.surfarray.blit_array(self.screen, rgb_array)

        # Scale and blit to window
        self.window.blit(pygame.transform.scale(self.screen, self.window.get_rect().size), (0, 0))
        pygame.display.flip()
