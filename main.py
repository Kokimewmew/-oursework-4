from src.utils import collecting_vacancies, creating_dictionary_list, creating_a_list_of_instances, saver_json, \
    filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies


def user_interaction():
    """Функция взаимодействия с пользователем"""
    search_query = input("Введите поисковый запрос: ")  # Пример: Python
    coll_vacancies = collecting_vacancies(search_query)

    vacancies_list = creating_dictionary_list(coll_vacancies)

    saver_json(vacancies_list)

    list_of_instances = creating_a_list_of_instances(vacancies_list)

    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()  # Пример: разработчик
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))

    filtered_vacancies = filter_vacancies(list_of_instances, filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    for item in top_vacancies:
        print(item)


user_interaction()
