class Vacancy:
    """Класс вакансии"""

    def __init__(self, title, desc, salary_from, salary_to, link):
        self.title = title
        self.desc = desc
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.__link = link

    def __str__(self):
        """Возвращает строку"""
        return f'''{self.title}
{self.desc}
Зарплата от {self.salary_from} до {self.salary_to}
{self.__link}
'''

    def __gt__(self, other):
        """Сравнение зарплаты и возвращение вакансии с большей зарплатой"""
        if self.salary_from is not None and other.salary_from is not None:
            if self.salary_from > other.salary_from:
                return self.salary_from
            else:
                return other.salary_from
        return "Зарплата не указана"

    def __lt__(self, other):
        """Сравнение зарплаты и возвращение вакансии с меньшей зарплатой"""
        if self.salary_from is not None and other.salary_from is not None:
            if self.salary_from < other.salary_from:
                return self.salary_from
            else:
                return other.salary_from
        return "Зарплата не указана"
