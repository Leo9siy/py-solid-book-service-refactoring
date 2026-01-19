from abc import ABC, abstractmethod

from app.models import Book


class CommandInterface(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs) -> str | None:
        pass


class DisplayInterface(ABC):
    @abstractmethod
    def display(self, book: Book, display_type: str) -> None:
        pass


class PrinterInterface(ABC):
    @abstractmethod
    def print_book(self, book: Book, print_type: str) -> None:
        pass


class SerializerInterface(ABC):
    @abstractmethod
    def serialize(self, book: Book, serialize_type: str) -> str:
        pass
