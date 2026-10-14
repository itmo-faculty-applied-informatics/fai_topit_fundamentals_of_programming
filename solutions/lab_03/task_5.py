"""Анализ результатов группы. Запуск: python task_5.py."""

from collections.abc import Sequence
from math import isclose


students = {
    "Анна": [78, 91, 84, 88],
    "Борис": [60, 72, 68],
    "Дарья": [95, 93, 97, 90],
    "Илья": [55, 61],
}

CATEGORIES = ("Отлично", "Хорошо", "Удовлетворительно", "Неудовлетворительно", "Нет результатов")


def mean(values: Sequence[float]) -> float | None:
    """Непустая последовательность чисел -> среднее; пустая -> None."""
    if not values:
        return None
    return sum(values) / len(values)


def minimum(values: Sequence[float]) -> float | None:
    """Последовательность чисел -> минимум без min(); пустая -> None."""
    if not values:
        return None
    result = values[0]
    for value in values[1:]:
        if value < result:
            result = value
    return result


def maximum(values: Sequence[float]) -> float | None:
    """Последовательность чисел -> максимум без max(); пустая -> None."""
    if not values:
        return None
    result = values[0]
    for value in values[1:]:
        if value > result:
            result = value
    return result


def classify(score: float | None) -> str:
    """Балл 0..100 -> категория; None -> 'Нет результатов'."""
    if score is None:
        return "Нет результатов"
    if not 0 <= score <= 100:
        raise ValueError("Балл должен находиться в диапазоне от 0 до 100")
    if score >= 90:
        return "Отлично"
    if score >= 75:
        return "Хорошо"
    if score >= 60:
        return "Удовлетворительно"
    return "Неудовлетворительно"


def student_summary(name: str, results: Sequence[float]) -> dict:
    """Имя и оценки 0..100 -> новый словарь итогов; пустые оценки допустимы."""
    for score in results:
        if not 0 <= score <= 100:
            raise ValueError("Оценки должны находиться в диапазоне от 0 до 100")
    average = mean(results)
    return {
        "name": name,
        "count": len(results),
        "mean": average,
        "minimum": minimum(results),
        "maximum": maximum(results),
        "category": classify(average),
    }


def find_top_students(students: dict[str, list[int]]) -> list[str]:
    """Группа -> имена всех лидеров в порядке ввода, без пустых результатов."""
    leaders = []
    best = None
    for name, results in students.items():
        average = student_summary(name, results)["mean"]
        if average is None:
            continue
        if best is None or average > best:
            best = average
            leaders = [name]
        elif average == best:
            leaders.append(name)
    return leaders


def group_summary(students: dict[str, list[int]]) -> dict:
    """Группа -> статистика, категории и рейтинг; исходный словарь не меняется."""
    summaries = [student_summary(name, results) for name, results in students.items()]
    categories = dict.fromkeys(CATEGORIES, 0)
    for summary in summaries:
        categories[summary["category"]] += 1
    # sorted создает новый список; при равенстве сохраняется порядок ввода.
    rating = sorted(
        [summary for summary in summaries if summary["mean"] is not None],
        key=lambda summary: summary["mean"],
        reverse=True,
    )
    all_results = [score for results in students.values() for score in results]
    leaders = []
    if rating:
        leaders = [row["name"] for row in rating if row["mean"] == rating[0]["mean"]]
    return {
        "student_count": len(students),
        "result_count": len(all_results),
        "mean": mean(all_results),
        "minimum": minimum(all_results),
        "maximum": maximum(all_results),
        "categories": categories,
        "leaders": leaders,
        "rating": rating,
    }


def format_report(student_data: Sequence[dict], group_data: dict) -> str:
    """Итоги student_summary и group_summary -> текст; пустая группа допустима."""
    def number(value: float | None) -> str:
        return "нет данных" if value is None else f"{value:.2f}"

    lines = ["Результаты студентов"]
    for row in student_data:
        lines.append(
            f"{row['name']}: среднее {number(row['mean'])}; "
            f"минимум {number(row['minimum'])}; максимум {number(row['maximum'])}; "
            f"категория: {row['category']}"
        )
    if not student_data:
        lines.append("Группа пуста")
    lines.extend([
        f"Студентов: {group_data['student_count']}; оценок: {group_data['result_count']}",
        f"Среднее группы: {number(group_data['mean'])}",
        f"Минимум группы: {number(group_data['minimum'])}; "
        f"максимум группы: {number(group_data['maximum'])}",
        "Лидеры: " + (", ".join(group_data["leaders"]) or "нет"),
        "Категории:",
    ])
    lines.extend(f"  {category}: {count}" for category, count in group_data["categories"].items())
    lines.append("Рейтинг:")
    lines.extend(
        f"  {position}. {row['name']} — {number(row['mean'])}"
        for position, row in enumerate(group_data["rating"], start=1)
    )
    if not group_data["rating"]:
        lines.append("  нет результатов")
    return "\n".join(lines)


def run_checks() -> None:
    # 1. Обычные данные, взвешенное по числу оценок среднее и неизменность.
    original = {name: results[:] for name, results in students.items()}
    group = group_summary(students)
    assert isclose(group["mean"], 1032 / 13)
    assert (group["minimum"], group["maximum"]) == (55, 97)
    assert find_top_students(students) == group["leaders"] == ["Дарья"]
    assert [row["name"] for row in group["rating"]] == ["Дарья", "Анна", "Борис", "Илья"]
    assert list(students.items()) == list(original.items())
    assert group["categories"] == dict(zip(CATEGORIES, [1, 1, 1, 1, 0]))
    assert mean([2, 4]) == 3
    assert minimum([5, 2, 8]) == 2
    assert maximum([5, 8, 2]) == 8
    report = format_report([student_summary(n, r) for n, r in students.items()], group)
    assert "Среднее группы: 79.38" in report and "Лидеры: Дарья" in report

    # 2. Один студент.
    single = {"Анна": [80]}
    assert student_summary("Анна", [80])["category"] == "Хорошо"
    assert group_summary(single)["mean"] == 80
    assert find_top_students(single) == ["Анна"]

    # 3. Несколько лидеров с разным количеством оценок.
    tied = {"Анна": [80, 100], "Борис": [90], "Илья": [60]}
    assert find_top_students(tied) == ["Анна", "Борис"]
    assert group_summary(tied)["leaders"] == ["Анна", "Борис"]

    # 4. Пустая группа.
    empty = group_summary({})
    assert empty["mean"] is None and empty["rating"] == []
    assert find_top_students({}) == []
    assert "Группа пуста" in format_report([], empty)
    assert mean([]) is minimum([]) is maximum([]) is None

    # 5. Пустые результаты отдельно и в смешанной группе.
    missing = student_summary("Илья", [])
    assert missing["mean"] is None and missing["category"] == "Нет результатов"
    assert find_top_students({"Илья": []}) == []
    mixed = group_summary({"Илья": [], "Анна": [100]})
    assert mixed["mean"] == 100 and mixed["categories"]["Нет результатов"] == 1
    assert [row["name"] for row in mixed["rating"]] == ["Анна"]
    assert "нет данных" in format_report([missing], group_summary({"Илья": []}))

    # 6. Границы категорий: на границе и непосредственно ниже нее.
    for score, category in [
        (0, "Неудовлетворительно"), (59.99, "Неудовлетворительно"),
        (60, "Удовлетворительно"), (74.99, "Удовлетворительно"),
        (75, "Хорошо"), (89.99, "Хорошо"), (90, "Отлично"), (100, "Отлично"),
        (None, "Нет результатов"),
    ]:
        assert classify(score) == category
    for score in (-1, 101):
        try:
            classify(score)
        except ValueError:
            pass
        else:
            raise AssertionError("Недопустимый балл должен вызвать ValueError")


if __name__ == "__main__":
    run_checks()
    student_data = [student_summary(name, results) for name, results in students.items()]
    print(format_report(student_data, group_summary(students)))
