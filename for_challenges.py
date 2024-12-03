# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']
# ???


# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём
# Пример вывода:
# Оля: 3
# Петя: 4

names = ['Оля', 'Петя', 'Вася', 'Маша']
# ???


# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
    'Оля': False,  # если False, то пол женский
    'Петя': True,  # если True, то пол мужской
    'Вася': True,
    'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']
# ???


# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.

groups = [
    ['Вася', 'Маша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
    ['Оля', 'Петя', 'Гриша'],
]
# ???


# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
# Пример вывода:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
    ['Вася', 'Маша'],
    ['Оля', 'Петя', 'Гриша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
]
# ???


# Вывод имени на каждой строке
def get_people_names(people_names):
    for people_name in people_names:
        print (f'{people_name}')


# Вывод имени с указанием количество символов
def get_count_letters(people_names):
    for people_name in people_names:
        print(f'{people_name} - {len(people_name)}')


# Вывод пола напротив имени
def get_sex_people(people_sex):
    for people_gender in people_sex:
        if is_male[people_gender]:
            print(f'{people_gender} - Мужской')
        else:
            print(f'{people_gender} - Женский')


# вывод групп и количество учеников
def get_count_people (people_groups):
    print(f'Общее количество групп - {len(people_groups)}')
    count = 0
    for one_group in people_groups:
        count += 1
        print(f'Количество учеников в группе {count} - {len(one_group)}')


# Вывод имен учеников в каждой группе
def get_name_people(people_groups):
    count = 0
    for one_group in people_groups:
        count += 1
        print(f'Имена учащихся в группе {count} - {', '.join(one_group)}')

get_people_names(names)
get_count_letters(names)
get_sex_people(is_male)
get_count_people (groups)
get_name_people(groups)
