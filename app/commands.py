from app.interfaces import (CommandInterface, DisplayInterface,
                            PrinterInterface, SerializerInterface)
from app.models import Book


class DisplayCommand(CommandInterface):
    def __init__(self, display: DisplayInterface) -> None:
        self.display = display

    def execute(self, book: Book, method_type: str) -> None:
        self.display.display(book, method_type)


class PrintCommand(CommandInterface):
    def __init__(self, printer: PrinterInterface) -> None:
        self.printer = printer

    def execute(self, book: Book, method_type: str) -> None:
        self.printer.print_book(book, method_type)


class SerializerCommand(CommandInterface):
    def __init__(self, serializer: SerializerInterface) -> None:
        self.serializer = serializer

    def execute(self, book: Book, method_type: str) -> str:
        return self.serializer.serialize(book, method_type)
