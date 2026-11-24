from core.people.person import Person
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.book import Book


class Reader(Person):
    def __init__(
        self,
        name: str,
        age: int
    ):
        super().__init__(name, age)
        self._books = []

    def add_book(
        self,
        book: Book
    ):
        self._books.append(book)
        if self not in book.get_readers():
            book.add_reader(self)

    def list_books(self) -> list:
        return self._books

    def remove_book(self, book: Book):
        self._books.remove(book)
