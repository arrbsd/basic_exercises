# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
# ???


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
# ???


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
# ???


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school_one = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male_one = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
# ???


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school_two = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male_two = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???


from collections import Counter

def new_list_names(student_names):
    # создание нового списка имен
    list_names = []
    for student in student_names:
        list_names.append(student['first_name'])
    return list_names


def most_name_common(student_names):
    names_count = new_list_names(student_names)
    return max(names_count, key=names_count.count)


# вывод количества повторений каждого имени
names_count = new_list_names(students)
for name, count_name in Counter(names_count).items():
     print (f'{name}: {count_name}')
print(Counter(names_count))


# вывод самого частого имени
print(most_name_common(students))


# вывод самых частых имен в каждом классе
count = 0
for one_class in school_students:
    count += 1
    print(f'Самое частое имя в классе {count}. {most_name_common(one_class)}')


# считаем мальчиков и девочек в каждом классе и создаем новый словарь
def count_gender(school, is_male):
    new_class = {}
    for one_class in school:
        girls = 0
        boys = 0
        for student in one_class['students']:
            name = student['first_name']
            if is_male[name]:
                boys += 1
            else:
                girls += 1
        new_class[one_class['class']] = {'Male': boys, 'Female': girls}
    return new_class


# выводим количество мальчиков и количество девочек по каждому классу
for classroom, class_gender in count_gender(school_one, is_male_one).items():
    print(f'В классе {classroom} мальчиков {class_gender["Male"]} девочек {class_gender["Female"]}')


# ищем в каком классе больше мальчиков, а в каком больше девочек
genders_in_school = count_gender(school_two, is_male_two)
max_boys=0
max_boys_in_class = 0
max_girls = 0
max_girls_in_class = 0
for gender_class, gender in genders_in_school.items():
    print(gender_class)
    if gender['Male'] > max_boys:
        max_boys = gender['Male']
        max_boys_in_class = gender_class
    if gender['Female'] > max_girls:
        max_girls = gender['Female']
        max_girls_in_class = gender_class

print(f'В классе {max_girls_in_class} больше всего девочек')
print(f'В классе {max_boys_in_class} больше всего мальчиков')
