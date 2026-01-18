from app.interfaces import CommandInterface


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class DisplayCommand(CommandInterface):
    def __init__(self, display):
        self.display = display

    def execute(self, book: Book, method_type: str):
        self.display.display(book, method_type)


class PrintCommand(CommandInterface):
    def __init__(self, printer):
        self.printer = printer

    def execute(self, book: Book, method_type: str):
        self.printer.print_book(book, method_type)


class SerializerCommand(CommandInterface):
    def __init__(self, serializer):
        self.serializer = serializer

    def execute(self, book: Book, method_type: str):
        return self.serializer.serialize(book, method_type)

