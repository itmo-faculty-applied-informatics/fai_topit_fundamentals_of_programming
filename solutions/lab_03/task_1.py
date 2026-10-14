"""Условия, классификация и обработка списка учебных записей."""

LEVELS = ("недостаточно", "удовлетворительно", "хорошо", "отлично")
RECORDS = [
    (0, "exam", 0), (59, "practice", 3),
    (60, "project", 0), (74, "exam", 3),
    (75, "practice", 0), (89, "project", 3),
    (90, "exam", 0), (100, "project", 3),
    (90, "practice", 4), (60, "exam", 5),
    (0, "unknown", 5), (101, "exam", 0),
]


def is_correct(score: int, worktype: str, skip: int) -> bool:
    """Проверяет диапазоны; неизвестный тип работы обрабатывается отдельно."""
    if score < 0 or score > 100:
        return False
    elif skip < 0 or skip > 5:
        return False
    else:
        return True


def pts2lvl(pts: int, skip: int = 0) -> int:
    """Корректные баллы и пропуски -> уровень 1..4 с учетом снижения."""
    if pts <= 59:
        level = 1
    elif pts <= 74:
        level = 2
    elif pts <= 89:
        level = 3
    else:
        level = 4
    if skip > 3 and level > 1:
        level -= 1
    return level


def scoring(lvl: int) -> str:
    """Уровень 1..4 -> текстовая категория."""
    return LEVELS[lvl - 1]


def typehelp(worktype: str) -> str:
    """Возвращает пояснение типа работы, включая неизвестный тип."""
    match worktype:
        case "exam":
            return "экзаменационная работа"
        case "project":
            return "проектная работа"
        case "practice":
            return "практическая работа"
        case _:
            return "неизвестный тип работы"


def gen_report(points: int, worktype: str, skips: int) -> str:
    """Корректная запись -> готовая строка результата."""
    return (f"Баллы студента: {points}. Пропусков: {skips}. "
            f"Оценка: {scoring(pts2lvl(points, skips))}. "
            f"Тип работы: {worktype} — {typehelp(worktype)}.")


def get_score(points: int, worktype: str, skips: int) -> str:
    """Проверяет диапазоны до классификации и формирует ответ."""
    if not is_correct(points, worktype, skips):
        return "Данные некорректны"
    return gen_report(points, worktype, skips)


def process_records(records: list[tuple[int, str, int]]) -> tuple[list[str], dict[str, int]]:
    """Не меняя записи, возвращает строки и счетчики, включая неверные записи."""
    reports = []
    counts = dict.fromkeys(LEVELS, 0)
    counts["некорректные данные"] = 0
    for score, worktype, skips in records:
        reports.append(get_score(score, worktype, skips))
        if not is_correct(score, worktype, skips):
            counts["некорректные данные"] += 1
            continue
        counts[scoring(pts2lvl(score, skips))] += 1
    return reports, counts


def run_checks() -> None:
    for score, expected in [(0, 1), (59, 1), (60, 2), (74, 2),
                            (75, 3), (89, 3), (90, 4), (100, 4)]:
        assert pts2lvl(score) == expected
        assert scoring(expected) in get_score(score, "exam", 0)
    assert pts2lvl(0, 5) == 1
    assert pts2lvl(90, 4) == 3
    for score, skips in [(-1, 0), (101, 0), (50, -1), (50, 6)]:
        assert get_score(score, "exam", skips) == "Данные некорректны"
    assert typehelp("unknown") == "неизвестный тип работы"
    assert typehelp("practice") == "практическая работа"
    assert typehelp("project") == "проектная работа"
    assert typehelp("exam") == "экзаменационная работа"
    before = RECORDS.copy()
    reports, counts = process_records(RECORDS)
    assert len(reports) == 12
    assert counts == {"недостаточно": 4, "удовлетворительно": 2,
                      "хорошо": 3, "отлично": 2, "некорректные данные": 1}
    assert RECORDS == before
    assert process_records([]) == ([], dict.fromkeys((*LEVELS, "некорректные данные"), 0))


def main() -> None:
    run_checks()
    try:
        points = int(input("Баллы: "))
        worktype = input("Тип работы: ")
        skips = int(input("Пропуски: "))
    except EOFError:
        print("Ввод завершен. Выполняется демонстрация списка.")
    else:
        print(get_score(points, worktype, skips))
    print("\nСписок учебных записей")
    reports, counts = process_records(RECORDS)
    print(*reports, sep="\n")
    print("Сводка:")
    for category, count in counts.items():
        print(f"{category}: {count}")


if __name__ == "__main__":
    main()
