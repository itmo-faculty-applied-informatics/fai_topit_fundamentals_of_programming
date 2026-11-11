records = [
    (95, "exam", 0),
    (90, "project", 4),
    (82, "practice", 1),
    (75, "exam", 5),
    (74, "project", 0),
    (60, "practice", 3),
    (65, "exam", 4),
    (59, "project", 2),
    (30, "practice", 5),
    (100, "exam", 5),
    (0, "project", 0),
    (88, "quiz", 2),
    (105, "exam", 1),
]


lines = []
count_excellent = 0
count_good = 0
count_satisfactory = 0
count_insufficient = 0
count_errors = 0

for number, (score, tipe, absences) in enumerate(records, start=1):

    # Часть 1. Проверка диапазонов
    if score < 0 or score > 100:
        lines.append(f"Запись {number}: Неправильный ввод балла.")
        count_errors += 1
        continue
    elif absences < 0 or absences > 5:
        lines.append(f"Запись {number}: Неправильный ввод количества пропусков.")
        count_errors += 1
        continue

    # Часть 2. Уровень: 3 - отличный, 2 - хороший, 1 - удовлетворительный, 0 - недостаточный
    if score >= 90:
        level = 3
    elif score >= 75:
        level = 2
    elif score >= 60:
        level = 1
    else:
        level = 0

    if absences > 3 and level > 0:
        level = level - 1

    if level == 3:
        level_name = "отличный"
        count_excellent += 1
    elif level == 2:
        level_name = "хороший"
        count_good += 1
    elif level == 1:
        level_name = "удовлетворительный"
        count_satisfactory += 1
    else:
        level_name = "недостаточный"
        count_insufficient += 1

    # Часть 3. Тип работы
    match tipe:
        case "exam":
            explanation = "экзаменационная работа"
        case "project":
            explanation = "проектная работа"
        case "practice":
            explanation = "практическая работа"
        case _:
            explanation = "неизвестный тип работы"

    lines.append(f"Запись {number}: {score} баллов, {absences} пропусков -> {level_name}, {explanation}")

# После цикла: два блока вывода
print("Индивидуальные результаты:")
for line in lines:
    print(line)

print("\n==Итоговая сводка==\n")
print("отличный:", count_excellent)
print("хороший:", count_good)
print("удовлетворительный:", count_satisfactory)
print("недостаточный:", count_insufficient)
print("ошибки ввода:", count_errors)
print("Всего записей:", len(records))


