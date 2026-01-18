import json

from app.interfaces import (DisplayInterface,
                            PrinterInterface, SerializerInterface)
import xml.etree.ElementTree as Etree

from app.main import Book


class Display(DisplayInterface):
    def display(self, book: Book, display_type: str) -> None:
        if display_type == "console":
            print(book.content)
        elif display_type == "reverse":
            print(book.content[::-1])
        else:
            raise ValueError(f"Unknown display type: {display_type}")


class Printer(PrinterInterface):
    def print_book(self, book: Book, print_type: str) -> None:
        if print_type == "console":
            print(f"Printing the book: {book.title}...")
            print(book.content)
        elif print_type == "reverse":
            print(f"Printing the book in reverse: {book.title}...")
            print(book.content[::-1])
        else:
            raise ValueError(f"Unknown print type: {print_type}")


class Serializer(SerializerInterface):
    def serialize(self, book: Book, serialize_type: str) -> str:
        if serialize_type == "json":
            return json.dumps({"title": book.title, "content": book.content})
        elif serialize_type == "xml":
            root = Etree.Element("book")
            title = Etree.SubElement(root, "title")
            title.text = book.title
            content = Etree.SubElement(root, "content")
            content.text = book.content
            return Etree.tostring(root, encoding="unicode")
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
