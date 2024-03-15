from abc import ABC, abstractmethod


class Rot(ABC):
    SHIFT: int = 0

    @abstractmethod
    def shift(self, char: str, shift_value: int) -> str:
        pass

    @abstractmethod
    def encrypt(self, text: str) -> str:
        pass

    @abstractmethod
    def decrypt(self, text: str) -> str:
        pass
