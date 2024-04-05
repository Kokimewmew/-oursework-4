class Vacancy:
    """Класс вакансии"""
    def __init__(self, title, desc, salary_from, salary_to, link):
        self.title = title
        self.desc = desc
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.link = link

    def __str__(self):
        """Возвращает строку"""
        return f'''{self.title}
{self.desc}
Зарплата от {self.salary_from} до {self.salary_to}
{self.link}
'''
