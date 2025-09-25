groupmates = [
    {
        'name': 'Артём',
        'surname': 'Бабушкин',
        'exams': ['asd', 'sdfg', 'sdff'],
        'marks': [4, 3, 5]
    },
    {
        'name': 'Артём',
        'surname': 'Бабушкин',
        'exams': ['asd', 'sdfg', 'sdff'],
        'marks': [3, 5, 3]
    },
    {
        'name': 'Артём',
        'surname': 'Бабушкин',
        'exams': ['asd', 'sdfg', 'sdff'],
        'marks': [5, 3, 5]
    }
]

def print_users(avg_mark, students):
    for student in students:
        avg = round(sum(student['marks'])/len(student['marks']),2)
        if avg > avg_mark:
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))

print_users(float(input()), groupmates)