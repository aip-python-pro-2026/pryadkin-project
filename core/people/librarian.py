from core.people.person import Person


CEO_SALARY = 100000


class Librarian(Person):
    def __init__(
        self,
        name: str,
        age: int,
        salary: int
    ):
        super().__init__(name, age)
        self.salary = salary

    @property
    def salary(self) -> int:
        return self._salary

    @salary.setter
    def salary(self, new_salary: int) -> None:
        if new_salary < 0:
            new_salary = -new_salary
        if new_salary > CEO_SALARY:
            new_salary = new_salary % CEO_SALARY
        if new_salary == 0:
            new_salary = 1000
        self._salary = new_salary

    def __str__(self):
        return 'Библиотекарь ' + self._name
