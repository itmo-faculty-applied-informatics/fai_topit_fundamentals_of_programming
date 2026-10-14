"""Коллекции попыток, согласованное обновление и текстовые запросы."""
submissions = [
    ("anna", "lab_01", 5), ("boris", "lab_01", 4),
    ("anna", "lab_02", 5), ("daria", "lab_01", 3),
    ("boris", "lab_02", 5), ("anna", "lab_01", 4),
]


def add_submission(data: dict, record: tuple[str, str, int]) -> None:
    """Добавляет запись и обновляет существующие индексы без перестроения."""
    student, lab, score = record
    key = (student, lab)
    data["submissions"].append(record)
    data["students"].add(student)
    data["labs"].add(lab)
    data["attempts"].setdefault(student, []).append((lab, score))
    data["completed"].setdefault(lab, set()).add(student)
    data["attempts_detailed"][key] = data["attempts_detailed"].get(key, 0) + 1
    if key not in data["best"] or score > data["best"][key]:
        data["best"][key] = score


def build_data(records: list[tuple[str, str, int]]) -> dict:
    """Создает все индексы за один проход, не меняя входной список."""
    data = dict(submissions=[], students=set(), labs=set(), attempts={},
                best={}, attempts_detailed={}, completed={})
    for record in records:
        add_submission(data, record)
    return data


def completed_both(data: dict, first: str, second: str) -> set[str]:
    """Возвращает пересечение сдававших две работы; неизвестная работа -> пусто."""
    return data["completed"].get(first, set()) & data["completed"].get(second, set())


def execute_query(data: dict, command: str) -> str:
    """Разбирает запрос; неверная команда/аргументы/ключ возвращают сообщение."""
    parts = command.split()
    if not parts:
        return "Введите команду"
    action, *args = parts
    argument_counts = {"student": 1, "best": 2, "attempts": 2, "completed": 1}
    if action not in argument_counts:
        return "Неизвестная команда"
    if len(args) != argument_counts[action]:
        return f"Неверное количество аргументов: {action}"
    if action == "student":
        if args[0] not in data["attempts"]:
            return "Студент не найден"
        return "\n".join(f"{lab}: {score}" for lab, score in data["attempts"][args[0]])
    if action == "completed":
        if args[0] not in data["completed"]:
            return "Лабораторная работа не найдена"
        return ", ".join(sorted(data["completed"][args[0]]))
    key = tuple(args)
    mapping = data["best"] if action == "best" else data["attempts_detailed"]
    if key not in mapping:
        return "Попытки не найдены"
    return str(mapping[key])


def run_checks() -> None:
    before = submissions.copy()
    data = build_data(submissions)
    assert data["students"] == {"anna", "boris", "daria"}
    assert data["labs"] == {"lab_01", "lab_02"}
    assert data["attempts"]["anna"] == [("lab_01", 5), ("lab_02", 5), ("lab_01", 4)]
    assert data["best"] == {("anna", "lab_01"): 5, ("anna", "lab_02"): 5,
                            ("boris", "lab_01"): 4, ("boris", "lab_02"): 5,
                            ("daria", "lab_01"): 3}
    assert data["attempts_detailed"] == {("anna", "lab_01"): 2, ("anna", "lab_02"): 1,
                                         ("boris", "lab_01"): 1, ("boris", "lab_02"): 1,
                                         ("daria", "lab_01"): 1}
    assert completed_both(data, "lab_01", "lab_02") == {"anna", "boris"}
    assert completed_both(data, "missing", "lab_02") == set()
    assert execute_query(data, "student anna") == "lab_01: 5\nlab_02: 5\nlab_01: 4"
    assert execute_query(data, "best anna lab_01") == "5"
    assert execute_query(data, "attempts boris lab_02") == "1"
    assert execute_query(data, "completed lab_01") == "anna, boris, daria"
    assert execute_query(data, "best nobody lab_01") == "Попытки не найдены"
    assert execute_query(data, "attempts nobody lab_01") == "Попытки не найдены"
    assert execute_query(data, "student nobody") == "Студент не найден"
    assert execute_query(data, "completed missing") == "Лабораторная работа не найдена"
    assert execute_query(data, "best") == "Неверное количество аргументов: best"
    assert execute_query(data, "student anna extra") == "Неверное количество аргументов: student"
    assert execute_query(data, "unknown") == "Неизвестная команда"
    assert execute_query(data, "  ") == "Введите команду"
    best_index = data["best"]
    add_submission(data, ("anna", "lab_01", 5))
    assert data["best"] is best_index
    assert data["attempts_detailed"][("anna", "lab_01")] == 3
    assert len(data["attempts"]["anna"]) == 4
    add_submission(data, ("eva", "lab_03", 4))
    assert "eva" in data["students"] and "lab_03" in data["labs"]
    assert data["completed"]["lab_03"] == {"eva"}
    assert data["best"][("eva", "lab_03")] == 4
    assert data == build_data(submissions + [("anna", "lab_01", 5), ("eva", "lab_03", 4)])
    assert build_data([])["students"] == set()
    assert submissions == before


def main() -> None:
    run_checks()
    data = build_data(submissions)
    for key in ("students", "labs", "attempts", "best", "attempts_detailed"):
        print(f"{key}: {data[key]}")
    print("Обе работы:", ", ".join(sorted(completed_both(data, "lab_01", "lab_02"))))
    new_record = ("anna", "lab_01", 5)
    add_submission(data, new_record)
    print("Добавлена запись:", new_record)
    for query in ("student anna", "best anna lab_01", "attempts boris lab_02", "completed lab_01"):
        print(f"> {query}\n{execute_query(data, query)}")
    print("Команды: student, best, attempts, completed; exit — выход")
    while True:
        try:
            command = input("$ ")
        except EOFError:
            break
        if command.strip() == "exit":
            break
        print(execute_query(data, command))


if __name__ == "__main__":
    main()
