

class Person:
    def __init__(
        self,
        name: str,
        age: int
    ) -> None:
        self._name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int):
        if age < 0:
            age = -age
        if age > 120:
            age = 120
        self._age = age

    def __str__(self) -> str:
        return self._name
