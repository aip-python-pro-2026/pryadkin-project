class Chapter:
    def __init__(self,
        number: int,
        text: str,
        name: str | None = None
    ):
        self._number = number
        self._text = text
        self._name = name

    def text(self) -> str:
        if self._name is None:
            return self._text
        return f'''Глава {self._number}. {self._name}
{self._text}'''

    def __str__(self):
        return self.text()
