from abc import ABC, abstractmethod


class Rot(ABC):
    def __init__(self, shift: int = None):
        self.shift = shift

    @abstractmethod
    def encrypt(self, text: str) -> str:
        pass

    @abstractmethod
    def decrypt(self, text: str) -> str:
        pass
