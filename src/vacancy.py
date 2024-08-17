class Vacancy:
    def __init__(self, name, url, salary_from, salary_to, description):
        self.name = name
        self.url = url
        self.salary_from = salary_from if salary_from else 0
        self.salary_to = salary_to if salary_to else 0
        self.description = description

    def __repr__(self):
        return f"Vacancy(name={self.name}, salary_from={self.salary_from}, salary_to={self.salary_to})"

    def __lt__(self, other):
        return self.salary_from < other.salary_from

    def __le__(self, other):
        return self.salary_from <= other.salary_from

    def __gt__(self, other):
        return self.salary_from > other.salary_from

    def __ge__(self, other):
        return self.salary_from >= other.salary_from

    def __eq__(self, other):
        return self.salary_from == other.salary_from and self.salary_to == other.salary_to
