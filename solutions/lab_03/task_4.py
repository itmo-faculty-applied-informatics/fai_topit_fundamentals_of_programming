def arithmetic_mean(values: list[float]) -> float | None:
    if len(values) == 0:
        return None
    total = 0
    for v in values:
        total += v
    return total / len(values)

assert arithmetic_mean([2, 4, 6]) == 4
assert arithmetic_mean([5]) == 5
assert arithmetic_mean([]) is None

def normalize_name(name: str) -> str:
    words = name.split()
    result = []
    for w in words:
        result.append(w.capitalize())
    return " ".join(result)

assert normalize_name("  иВАН   пЕтРоВ ") == "Иван Петров"
assert normalize_name("анна") == "Анна"
assert normalize_name("   ") == ""



def build_report(
    student: str,
    results: list[int],
    *,
    precision: int = 2,
    prefix: str = "Результат",
) -> str:
    if not results:
        return f"{prefix}: {student} — нет результатов"

    mean = arithmetic_mean(results)
    return (
        f"{prefix}: {student} — среднее {mean:.{precision}f}, "
        f"минимум {min(results)}, максимум {max(results)}, "
        f"количество {len(results)}"
    )


def collect_tags(*tags: str, lowercase: bool = True) -> tuple[str, ...]:
    seen: set[str] = set()
    result: list[str] = []

    for tag in tags:
        cleaned = tag.strip()
        if lowercase:
            cleaned = cleaned.lower()
        if not cleaned:
            continue
        if cleaned in seen:
            continue
        seen.add(cleaned)
        result.append(cleaned)

    return tuple(result)


# проверки build_report
assert build_report("Анна", [5, 4, 5]) == \
    "Результат: Анна — среднее 4.67, минимум 4, максимум 5, количество 3"
assert build_report("Анна", [5, 4, 5], precision=1, prefix="Итог") == \
    "Итог: Анна — среднее 4.7, минимум 4, максимум 5, количество 3"
assert build_report("Борис", []) == "Результат: Борис — нет результатов"
assert build_report("Анна", [5, 4, 5], precision=0).startswith("Результат: Анна — среднее 5,")

# проверки collect_tags
assert collect_tags("Python", " python ", "") == ("python",)
assert collect_tags("A", "a", lowercase=False) == ("A", "a")
assert collect_tags() == ()
assert collect_tags("  ", "") == ()


# распаковка списка через * и словаря через **
tag_list = ["Python", "python", "Algo", " "]
print(collect_tags(*tag_list))

options = {"precision": 1, "prefix": "Итог"}
print(build_report("Борис", [4, 3, 5], **options))

# Исследование LEGB

course = "Алгоритмы"


def outer():
    attempts = 0

    def inner():
        nonlocal attempts
        attempts += 1
        note = f"{course}: попытка {attempts}"
        print(note)

    inner()
    inner()
    print("attempts в outer:", attempts)
    return attempts


result = outer()
print("course после вызова:", course)
assert course == "Алгоритмы"
assert result == 2

def add_result_buggy(value, results=[]):
    results.append(value)
    return results


def add_result(value, results=None):
    if results is None:
        results = []
    results.append(value)
    return results


# демонстрация ошибки
add_result_buggy(1)
second = add_result_buggy(2)
assert second == [1, 2]

# исправленная версия
add_result(1)
assert add_result(2) == [2]

# Практическая часть
def apply_to_results(operation, values):
    applied = []
    for item in values:
        applied.append(operation(item))
    return applied


def make_threshold_checker(threshold):
    def check(score):
        return score >= threshold
    return check


def add_bonus(score):
    return min(score + 5, 100)


scores = [70, 85, 98]

# именованная функция и lambda
with_bonus = apply_to_results(add_bonus, scores)
as_fraction = apply_to_results(lambda s: s / 100, scores)

print(with_bonus)
print(as_fraction)

assert with_bonus == [75, 90, 100]
assert as_fraction == [0.7, 0.85, 0.98]
assert scores == [70, 85, 98]


passed = make_threshold_checker(60)
excellent = make_threshold_checker(90)

print(passed(75), excellent(75))
print(passed(95), excellent(95))

assert passed(60) is True
assert passed(59) is False
assert excellent(90) is True
assert excellent(89) is False

print(apply_to_results(passed, [55, 60, 75]))