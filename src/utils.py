from src.hh_api_class import HeadHunterParser
from src.saver import JSONSaver
from src.vacancy import Vacancy


def collecting_vacancies(user_input):
    """Функция для сбора вакансии по запросу"""
    parser = HeadHunterParser()

    search_query = user_input
    datas = parser.get_vacancies(search_query)
    return datas


def creating_dictionary_list(other):
    """Функция для создания списка словарей по атрибутам"""
    vacancies_list = []
    for item in other['items']:
        salary_from = item['salary'].get('from') if item['salary'] else None
        salary_to = item['salary'].get('to') if item['salary'] else None
        vacancies_list.append(
            {"title": item['name'], "desc": item['area']['name'], "salary_from": salary_from, "salary_to": salary_to,
             "link": item['area']['url']})

    return vacancies_list


def creating_a_list_of_instances(other):
    """Функция для создания списка экземпляров класса Vacancy"""
    vacancies_list = []
    for item in other:
        vacancy_ex = Vacancy(item["title"], item["desc"], item["salary_from"], item["salary_to"], item["link"])
        vacancies_list.append(vacancy_ex)

    return vacancies_list


def saver_json(other):
    """Функция записи списка экземпляров в JSON"""
    saver = JSONSaver()
    saver.insert(other)


def filter_vacancies(list_of_instances, filter_words):
    """Функция фильтрации по ключевому слову пользователя"""
    list_file = []
    for instance in list_of_instances:
        for word in filter_words:
            if word.lower().strip() in instance.title.lower():
                list_file.append(instance)
                break
    return list_file


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    """Функция фильтрации по диапазону зарплаты"""
    try:
        min_salary, max_salary = map(int, salary_range.split('-'))
        ranged_vacancies = []
        for vacancies in filtered_vacancies:
            if vacancies.salary_from is None:
                vacancies.salary_from = 0
            if vacancies.salary_to is None:
                vacancies.salary_to = 0
            if vacancies.salary_from >= min_salary and vacancies.salary_to <= max_salary:
                ranged_vacancies.append(vacancies)
        return ranged_vacancies
    except ValueError:
        print("Диапазон выбран некорректно")


def sort_vacancies(ranged_vacancies):
    """Функция сортировки зарплат от"""
    sorted_vacancies = sorted(ranged_vacancies, key=lambda x: x.salary_from, reverse=True)
    return sorted_vacancies


def get_top_vacancies(sorted_vacancies, top_n):
    """Функция возвращает рейтинг указанный пользователем """
    return sorted_vacancies[:top_n]
