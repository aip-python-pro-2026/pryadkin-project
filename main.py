from typing import Any

from core.book import Book
from core.chapter import Chapter

l: list[int | float] = [1, 3, 5.5]
t: tuple[int, int, float | int] = (1, 3, 5.5)
d: dict[str, Any] = {
    "data": "123",
    "data2": 321
}


def function(
    a: int | float,
    b: int | float
) -> int | float:
    """
    Функция, которая суммирует 2 числа и число 5
    :arg a: int первое число
    :arg b: int второе число
    :return сумма a + b + 5
    """
    c: int = 5
    return a + b + c


def main():
    # print(function(1.5, function(3, 5)))
    garry = Book(
        'Joanne Rowling',
        'Harry Potter',
        '26 июня 1997',
        [
            Chapter(
                1,
                'В далёком-далёком лесу',
                'Лес'
            )
        ],
        'fantasy'
    )
    # garry.__name = 'Parry Hotter'
    # print(garry.name())
    # print(dir(garry))
    print(garry)


if __name__ == "__main__":
    main()
