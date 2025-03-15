# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
print('Задание 1:')
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

name_count = {}

for student in students:
    name = student['first_name']
    if name in name_count:
        name_count[name] += 1
    else:
        name_count[name] = 1

for name in name_count:
    print(f'{name}: {name_count[name]}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
print('\nЗадание 2:')
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
# Создаю пустой словарь
name_count = {}

# Заполняю словарь Имя:Количество
for student in students:
    name = student['first_name']
    if name in name_count:
        name_count[name] += 1
    else:
        name_count[name] = 1
# Ввожу переменные для корректной работы в цикле
max_count = 0  # Счетчик вхождений имени
most_common_name = None # В переменную будет записываться самое популярное на текущий момент имя


for name, count in name_count.items():
    if count >= max_count:
        max_count = count
        most_common_name = name

print(f'Самое частое имя среди учеников: {most_common_name}')
# most_common_name = max(name_count, key=name_count.get)
# Нашел такой способ в интернете, но уже после того, как написал этот ужас :(


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша
print('\nЗадание 3:')
school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],
    [  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

for class_id, class_students in enumerate(school_students, start=1):
    name_count = {}

    for student in class_students:
        name = student['first_name']
        if name in name_count:
            name_count[name] += 1
        else:
            name_count[name] = 1
    
    most_common_name = max(name_count, key=name_count.get)
    print(f'Самое частое имя в классе {class_id}: {most_common_name}')

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2
print('\nЗадание 4:')
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for class_info in school:
    class_name = class_info['class']  # Не уверен, что правильно хранить название класса в отдельной переменной, сделал для упрощения f'строки
    students = class_info['students']

    count_male = 0
    count_female = 0

    for student in students:
        first_name = student['first_name']
        if is_male[first_name] == True:
            count_male += 1
        if is_male[first_name] == False:
            count_female += 1
    print(f'Класс {class_name}: {count_female} девочек и {count_male} мальчиков')


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
print('\nЗадание 5:')
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

max_male_class = None
max_female_class = None
max_male = 0
max_female = 0

for class_info in school:
    class_name = class_info['class']
    students = class_info['students']

    male_count = 0
    female_count = 0

    for student in students:
        first_name = student['first_name']
        if is_male[first_name] == True:
            male_count += 1
        if is_male[first_name] == False:
            female_count += 1

        if male_count > max_male:
            max_male = male_count
            max_male_class = class_name
        if female_count > max_female:
            max_female = female_count
            max_female_class = class_name
        
print(f'Больше всего мальчиков в классе {max_male_class}')
print(f'Больше всего девочек в классе {max_female_class}')


