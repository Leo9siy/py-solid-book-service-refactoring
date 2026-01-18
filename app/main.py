
class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    from app.services import Display, Printer, Serializer

    display = Display()
    printer = Printer()
    serializer = Serializer()

    for cmd, method_type in commands:
        if cmd == "display":
            display.display(book, method_type)
        elif cmd == "print":
            printer.print_book(book, method_type)
        elif cmd == "serialize":
            return serializer.serialize(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
