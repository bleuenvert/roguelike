# Define generic entity

from typing import Tuple


class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """
    # char is what character is used as the character model ie "T" for troll?
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx: int, dy: int) -> None:
        # Move the entity by a given amount
        self.x += dx
        self.y += dy
