from abc import ABC, abstractmethod


class ScreenInterface(ABC):
    @abstractmethod
    def display(self, display_type: str):
        pass


class PrinterInterface(ABC):
    @abstractmethod
    def print_book(self, print_type: str) -> None:
        pass


class SerializerInterface(ABC):
    @abstractmethod
    def serialize(self, serialize_type: str) -> str:
        pass
