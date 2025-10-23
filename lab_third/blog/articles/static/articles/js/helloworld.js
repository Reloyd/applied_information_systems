// articles/static/articles/js/helloworld.js

// Создаём массив студентов
var groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "group": "БВТ1702",
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "group": "БСТ1702",
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "group": "БАП1801",
        "marks": [5, 5, 5]
    }
];

// Функция для выравнивания строк
var rpad = function(str, length) {
    str = str.toString();
    while (str.length < length)
        str = str + ' ';
    return str;
};

// Функция вывода студентов
var printStudents = function(students) {
    console.log(
        rpad("Имя", 15),
        rpad("Фамилия", 15),
        rpad("Группа", 10),
        rpad("Оценки", 20)
    );
    for (var i = 0; i < students.length; i++) {
        console.log(
            rpad(students[i].name, 15),
            rpad(students[i].surname, 15),
            rpad(students[i].group, 10),
            rpad(students[i].marks.join(", "), 20)
        );
    }
    console.log('\n');
};

// Выводим всех студентов
printStudents(groupmates);

// Фильтрация по группе
var filterByGroup = function(students, group) {
    return students.filter(function(s) { return s.group === group; });
};

// Фильтрация по среднему баллу
var filterByAverage = function(students, minAvg) {
    return students.filter(function(s) {
        var avg = s.marks.reduce((a, b) => a + b) / s.marks.length;
        return avg >= minAvg;
    });
};

// Ввод от пользователя
var groupInput = prompt("Введите группу для фильтрации:");
if (groupInput) {
    console.log("Студенты группы " + groupInput + ":");
    printStudents(filterByGroup(groupmates, groupInput));
}

var avgInput = parseFloat(prompt("Введите минимальный средний балл:"));
if (!isNaN(avgInput)) {
    console.log("Студенты со средним баллом выше " + avgInput + ":");
    printStudents(filterByAverage(groupmates, avgInput));
}
