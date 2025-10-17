groupmates = [
    {
        'name': 'Артём',
        'surname': 'Бабушкин',
        'exams': ['История', 'Алгебра', 'Геометрия'],
        'marks': [4, 5, 4]
    },
    {
        'name': 'Данила',
        'surname': 'Мокров',
        'exams': ['Математика', 'Физика', 'Физ-ра'],
        'marks': [4, 5, 3]
    },
    {
        'name': 'Илья',
        'surname': 'Образумов',
        'exams': ['Обществознание', 'География', 'Изо'],
        'marks': [5, 5, 5]
    },
    {
        'name': 'Анна',
        'surname': 'Харченко',
        'exams': ['Математика', 'Физика', 'Физ-ра'],
        'marks': [4, 3, 3]
    },
    {
        'name': 'Александра',
        'surname': 'Дубровская',
        'exams': ['Обществознание', 'География', 'Изо'],
        'marks': [5, 4, 5]
    }
]

def print_users(avg_mark, students):
    for student in students:
        avg = round(sum(student['marks'])/len(student['marks']),2)
        if avg > avg_mark:
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))

print_users(float(input('Введите средний балл: ')), groupmates)