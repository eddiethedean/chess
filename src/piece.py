from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, color: Color) -> None:
        self.color: Color = color
    
    @abstractmethod
    def move(self, x: int, y: int) -> None:
        ...
