import json

from app.interfaces import (
    PrinterInterface, SerializerInterface, DisplayInterface)
import xml.etree.ElementTree as Etree

from app.models import Book


class Display(DisplayInterface):
    def display(self, book: Book, display_type: str) -> None:
        if display_type == "console":
            self.display_console(book)
        elif display_type == "reverse":
            self.display_reverse(book)
        else:
            raise ValueError(f"Unknown display type: {display_type}")

    def display_console(self, book: Book):
        print(book.content)

    def display_reverse(self, book: Book):
        print(book.content[::-1])


class Printer(PrinterInterface):
    def print_book(self, book: Book, print_type: str) -> None:
        if print_type == "console":
            self.print_console(book)
        elif print_type == "reverse":
            self.print_reverse(book)
        else:
            raise ValueError(f"Unknown print type: {print_type}")

    def print_console(self, book: Book):
        print(f"Printing the book: {book.title}...")
        print(book.content)

    def print_reverse(self, book: Book):
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class Serializer(SerializerInterface):
    def serialize(self, book: Book, serialize_type: str) -> str:
        if serialize_type == "json":
            return self.serialize_json(book)
        elif serialize_type == "xml":
            return self.serialize_xml(book)
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")

    def serialize_json(self, book: Book):
        return json.dumps({"title": book.title, "content": book.content})
    def serialize_xml(self, book: Book):
        root = Etree.Element("book")
        title = Etree.SubElement(root, "title")
        title.text = book.title
        content = Etree.SubElement(root, "content")
        content.text = book.content
        return Etree.tostring(root, encoding="unicode")

