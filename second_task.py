import logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO)

class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year

    def value_of(self):
        return f'Book title : {self.title}, author name: {self.author}, publication year: {self.year}'


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass

class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        logging.info(f" The book '{book.title}' from '{book.author}' published in '{book.year}' has been added.")

    def remove_book(self, title: str) -> None:
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                break

    def show_books(self) -> None:
        if self.books:
            logging.info("Titles of books in library:")
            for book in self.books:
                logging.info(book.value_of())
        else:
            logging.info("Library is empty.")

class LibraryManager:
    def __init__(self, library: Library):
        self.library = library

    def add_book(self,book: Book) -> None:
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        self.library.show_books()

def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = (
            input("Enter command (add, remove, show, exit): ")
            .strip()
            .lower()
        )

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()

                book = Book(title, author, int(year))
                manager.add_book(book)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logging.info("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
