from app.commands import DisplayCommand, PrintCommand, SerializerCommand
from app.models import Book
from app.services import Display, Printer, Serializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display = Display()
    printer = Printer()
    serializer = Serializer()

    class_commands = {
        "display": DisplayCommand(display),
        "print": PrintCommand(printer),
        "serialize": SerializerCommand(serializer)
    }

    for cmd, method_type in commands:
        if cmd == "serialize":
            return class_commands.get("serialize").execute(book, method_type)

        class_commands.get(cmd).execute(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
