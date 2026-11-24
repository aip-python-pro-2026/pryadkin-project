from core.chapter import Chapter
from core.people.reader import Reader


class Book:
    def __init__(
        self,
        author: str,
        name: str,
        date: str,
        chapters: list[Chapter],
        genre: str
    ):
        self.__author = author
        self.__name = name
        self.__date = date
        self.__chapters = chapters
        self.__genre = genre
        self.__reader: list[Reader] = []

    def author(self) -> str:
        return self.__author

    def name(self) -> str:
        return self.__name

    def date(self) -> str:
        return self.__date

    def chapters(self) -> list[Chapter]:
        return self.__chapters

    def genre(self) -> str:
        return self.__genre

    def text(self):
        text: list[str] = []
        for chapter in self.chapters():
            text.append(str(chapter))
        return '\n\n'.join(text)

    def add_reader(self, reader: Reader):
        self.__reader.append(reader)
        if self not in reader.list_books():
            reader.add_book(self)

    def get_readers(self) -> list[Reader]:
        return self.__reader

    def __repr__(self):
        return f'''{self.__name} от {self.__author}
{self.text()}'''

    def __str__(self):
        return self.__repr__()
