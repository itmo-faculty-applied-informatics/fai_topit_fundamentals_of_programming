students = {
    "Анна": [78, 91, 84, 88],
    "Борис": [60, 72, 68],
    "Дарья": [95, 93, 97, 90],
    "Илья": [55, 61],
}

CATEGORIES = ("отличный", "хороший", "удовлетворительный", "недостаточный", "нет данных")


def mean(values):
    if not values:
        return None
    total = 0
    for value in values:
        total += value
    return total / len(values)


def minimum(values):
    if not values:
        return None
    result = values[0]
    for value in values:
        if value < result:
            result = value
    return result


def maximum(values):
    if not values:
        return None
    result = values[0]
    for value in values:
        if value > result:
            result = value
    return result


def classify(score):
    if score is None:
        return "нет данных"
    if score >= 90:
        return "отличный"
    if score >= 75:
        return "хороший"
    if score >= 60:
        return "удовлетворительный"
    return "недостаточный"


def student_summary(name, results):
    average = mean(results)
    return {
        "name": name,
        "count": len(results),
        "mean": average,
        "min": minimum(results),
        "max": maximum(results),
        "category": classify(average),
    }


def find_top_students(students):
    best = None
    top = []
    for name, results in students.items():
        average = mean(results)
        if average is None:
            continue
        average = round(average, 6)
        if best is None or average > best:
            best = average
            top = [name]
        elif average == best:
            top.append(name)
    return top


def group_summary(students):
    total = 0
    count = 0
    categories = {}
    for category in CATEGORIES:
        categories[category] = 0

    for results in students.values():
        for value in results:
            total += value
            count += 1
        categories[classify(mean(results))] += 1

    return {
        "students_count": len(students),
        "results_count": count,
        "group_mean": total / count if count else None,
        "categories": categories,
        "top": find_top_students(students),
    }


def make_rating(students):
    with_data = []
    without_data = []
    for name, results in students.items():
        summary = student_summary(name, results)
        if summary["mean"] is None:
            without_data.append(summary)
        else:
            with_data.append(summary)
    with_data = sorted(with_data, key=lambda item: item["mean"], reverse=True)
    return with_data + without_data


def fmt(value):
    if value is None:
        return "—"
    return f"{value:.2f}"


def format_report(student_data, group_data):
    lines = ["РЕЙТИНГ СТУДЕНТОВ"]
    if not student_data:
        lines.append("  студентов нет")
    for place, item in enumerate(student_data, start=1):
        lines.append(
            f"  {place}. {item['name']}: среднее {fmt(item['mean'])}, "
            f"мин {fmt(item['min'])}, макс {fmt(item['max'])}, "
            f"категория: {item['category']}"
        )

    lines.append("")
    lines.append("СВОДКА ПО ГРУППЕ")
    lines.append(f"  Студентов: {group_data['students_count']}")
    lines.append(f"  Общий средний результат: {fmt(group_data['group_mean'])}")
    if group_data["top"]:
        lines.append("  Лидер(ы): " + ", ".join(group_data["top"]))
    else:
        lines.append("  Лидер(ы): нет")
    lines.append("  По категориям:")
    for category, number in group_data["categories"].items():
        lines.append(f"    {category}: {number}")
    return "\n".join(lines)


def run(data):
    return format_report(make_rating(data), group_summary(data))


# сценарии проверки

# 1. обычный набор данных
copy_before = {name: list(results) for name, results in students.items()}
rating = make_rating(students)
assert [item["name"] for item in rating] == ["Дарья", "Анна", "Борис", "Илья"]
assert group_summary(students)["top"] == ["Дарья"]
assert group_summary(students)["categories"]["отличный"] == 1
assert students == copy_before  # исходные данные не изменены

# 2. один студент
single = {"Олег": [80, 90]}
assert group_summary(single)["top"] == ["Олег"]
assert group_summary(single)["group_mean"] == 85
assert student_summary("Олег", [80, 90])["category"] == "хороший"

# 3. несколько лидеров
tie = {"А": [90, 80], "Б": [85, 85], "В": [50]}
assert group_summary(tie)["top"] == ["А", "Б"]

# 4. пустая группа
empty = {}
empty_summary = group_summary(empty)
assert empty_summary["students_count"] == 0
assert empty_summary["group_mean"] is None
assert empty_summary["top"] == []
assert "студентов нет" in run(empty)

# 5. студент без результатов
with_empty = {"Аня": [70, 80], "Пусто": []}
item = student_summary("Пусто", [])
assert item["mean"] is None and item["min"] is None and item["max"] is None
assert item["category"] == "нет данных"
assert group_summary(with_empty)["top"] == ["Аня"]
assert group_summary(with_empty)["group_mean"] == 75
assert make_rating(with_empty)[-1]["name"] == "Пусто"

# 6. граничные значения категорий
assert classify(59) == "недостаточный"
assert classify(60) == "удовлетворительный"
assert classify(74) == "удовлетворительный"
assert classify(75) == "хороший"
assert classify(89) == "хороший"
assert classify(90) == "отличный"
assert classify(100) == "отличный"
assert classify(0) == "недостаточный"

# минимум и максимум
assert minimum([5, 3, 9]) == 3
assert maximum([5, 3, 9]) == 9
assert minimum([]) is None and maximum([]) is None

# вывод
print(run(students))
print("\nВсе проверки пройдены")
