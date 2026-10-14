"""Функции и области видимости на данных из task_3.py."""

from collections.abc import Callable, Sequence


def arithmetic_mean(values: list[float]) -> float:
    """Возвращает среднее; для пустого списка — резервное значение 0.0."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def normalize_name(name: str) -> str:
    """Удаляет лишние пробелы и приводит части имени к заглавному регистру."""
    if not name.strip():
        return ""
    return " ".join(part.title() for part in name.split())


def build_report(
    student: str,
    results: list[int],
    *,
    precision: int = 2,
    prefix: str = "Результат",
) -> str:
    """Формирует отчет со средним баллом; пустые данные обрабатывает отдельно."""
    student = normalize_name(student)

    if not student:
        return "Не указано имя студента"
    if precision < 0:
        return "Точность должна быть неотрицательной"
    if not results:
        return f"{prefix}: {student} — нет результатов"
    
    mean = arithmetic_mean(results)
    return f"{prefix}: {student} — {mean:.{precision}f}"


def collect_tags(*tags: str, lowercase: bool = True) -> tuple[str, ...]:
    """Очищает теги, удаляет пустые и повторы, сохраняя порядок появления."""
    if not tags:
        return ()
    cleaned = []
    for tag in tags:
        tag = tag.strip()
        if lowercase:
            tag = tag.lower()
        if tag and tag not in cleaned:
            cleaned.append(tag)
    return tuple(cleaned)


course = "Основы программирования"


def scope_demo() -> tuple[str, str]:
    local_course = "Лабораторная 3"

    def update_course() -> str:
        nonlocal local_course
        local_course = "Лабораторная 4"
        return f"{course}: {local_course}"

    message = update_course()
    return local_course, message


def add_result(value: int, results: list[int] | None = None) -> list[int]:
    """Возвращает новый список, не меняя переданный."""
    if results is None:
        return [value]
    return [*results, value]


def apply_to_results(
    operation: Callable[[int], int], values: Sequence[int]
) -> list[int]:
    """Применяет operation к каждому результату и создает новый список."""
    if not values:
        return []
    return [operation(value) for value in values]


def make_threshold_checker(threshold: int) -> Callable[[int], bool]:
    """Создает проверку достижения заданного порога."""
    def check(result: int) -> bool:
        return result >= threshold

    return check


def increase_result(value: int) -> int:
    return value + 1


def run_checks() -> None:
    values = [3, 4, 5]
    assert arithmetic_mean(values) == 4.0
    assert arithmetic_mean([2.5, 3.5]) == 3.0
    assert arithmetic_mean([]) == 0.0
    assert values == [3, 4, 5]

    assert normalize_name("  aNNa   ivANOVA  ") == "Anna Ivanova"
    assert normalize_name(name=" бОРИС ") == "Борис"
    assert normalize_name(" \t ") == ""

    assert build_report("anna", values) == "Результат: Anna — 4.00"
    assert build_report(student="boris", results=[4, 5], precision=1,
                        prefix="Среднее") == "Среднее: Boris — 4.5"
    assert build_report("daria", []) == "Результат: Daria — нет результатов"
    assert build_report(" ", [5]) == "Не указано имя студента"
    assert build_report("anna", [5], precision=-1) == "Точность должна быть неотрицательной"
    assert values == [3, 4, 5]

    assert collect_tags(" Lab_01 ", "lab_01", "", " lab_02 ") == ("lab_01", "lab_02")
    assert collect_tags("Anna", "anna", lowercase=False) == ("Anna", "anna")
    assert collect_tags() == ()
    assert collect_tags(" ", "\t") == ()

    assert add_result(5) == [5]
    assert add_result(4) == [4]
    assert add_result(2, values) == [3, 4, 5, 2]
    assert values == [3, 4, 5]

    assert apply_to_results(increase_result, values) == [4, 5, 6]
    assert apply_to_results(lambda value: value * 2, (3, 4)) == [6, 8]
    assert apply_to_results(increase_result, []) == []
    assert values == [3, 4, 5]

    passed = make_threshold_checker(3)
    excellent = make_threshold_checker(5)
    assert passed(3)
    assert not excellent(3)
    assert excellent(5)
    assert not passed(2)
    assert increase_result(0) == 1
    assert increase_result(4) == 5
    assert increase_result(-1) == 0

    assert scope_demo()[0] == "Лабораторная 4"
    assert scope_demo()[1] == "Основы программирования: Лабораторная 4"
    assert course == "Основы программирования"


def main() -> None:
    # Исходные записи из task_3.py, до демонстрационного append с оценкой 100.
    submissions = [
        ("anna", "lab_01", 5),
        ("boris", "lab_01", 4),
        ("anna", "lab_02", 5),
        ("daria", "lab_01", 3),
        ("boris", "lab_02", 5),
        ("anna", "lab_01", 4),
    ]
    students = sorted({student for student, lab, score in submissions})
    options = {"precision": 1, "prefix": "Средний балл"}
    passed = make_threshold_checker(3)
    excellent = make_threshold_checker(5)
    for student in students:
        results = [score for name, lab, score in submissions if name == student]
        print(build_report(student, results, **options))
        print("С прибавкой:", apply_to_results(increase_result, results))
        print("В процентах:", apply_to_results(lambda score: score * 20, results))
        print("Зачет:", [passed(score) for score in results])
        print("Отлично:", [excellent(score) for score in results])
    tags = [lab for student, lab, score in submissions]
    print("Лабораторные:", collect_tags(*tags, lowercase=True))
    print(scope_demo()[1])


if __name__ == "__main__":
    run_checks()
    main()
