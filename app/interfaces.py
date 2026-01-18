from abc import ABC, abstractmethod


class CommandInterface(ABC):
    @abstractmethod
    def execute(self, book, method_type: str) -> str | None:
        pass


class DisplayInterface(ABC):
    @abstractmethod
    def display(self, book, display_type: str) -> None:
        pass


class PrinterInterface(ABC):
    @abstractmethod
    def print_book(self, book, print_type: str) -> None:
        pass


class SerializerInterface(ABC):
    @abstractmethod
    def serialize(self, book, serialize_type: str) -> str:
        pass
