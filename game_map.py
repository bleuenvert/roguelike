# Defines the map class in terms of tiles

import numpy as np #type: ignore
from tcod.console import Console

import tile_types



class GameMap:
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=tile_types.floor, order="F")
        # this hardcodes in some walls for demonstration purposes.
        self.tiles[30:33, 22] = tile_types.wall

    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside of the bounds of this map"""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        # This is a method of console. It can draw the whole screen much faster than using console.print
        console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]
