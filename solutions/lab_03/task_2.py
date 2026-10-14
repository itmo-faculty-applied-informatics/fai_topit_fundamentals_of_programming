"""Статистика, поиск, проверка простоты и сортировка выбором."""
from collections.abc import Callable

measurements = [12, 15, 11, 18, 18, 9, 21, 15, 7, 18]


def measurement_summary(values: list[int]) -> dict:
    """Два прохода; для пустого списка среднее и экстремумы равны None."""
    if not values:
        return dict(total=0, minimum=None, maximum=None, even=0, count=0,
                    mean=None, above_mean=0)
    total = even = count = 0
    smallest = largest = values[0]
    for value in values:
        total += value
        count += 1
        if value < smallest:
            smallest = value
        if value > largest:
            largest = value
        if value % 2 == 0:
            even += 1
    average = total / count
    above = 0
    for value in values:
        if value > average:
            above += 1
    return dict(total=total, minimum=smallest, maximum=largest, even=even,
                count=count, mean=average, above_mean=above)


def linear_search(content: list[int], value: int) -> tuple[int, int]:
    """Индекс первого совпадения или -1 и число сравнений элементов с целью."""
    comparisons = 0
    for index, element in enumerate(content):
        comparisons += 1
        if element == value:
            return index, comparisons
    return -1, comparisons


def bin_search(content: list[int], caching: bool = False) -> Callable[[int], tuple[int, int]]:
    """Фабрика поиска в отсортированном списке; возвращает (индекс, сравнения).

    При повторах допустимо любое совпадение. После создания поиска список
    изменять нельзя. Кэш хранит индексы; попадание требует 0 сравнений с элементами.
    """
    cache = {}

    def search(value: int) -> tuple[int, int]:
        if caching and value in cache:
            return cache[value], 0
        left, right = 0, len(content)
        comparisons = 0
        index = -1
        while left < right:
            middle = (left + right) // 2
            comparisons += 1
            if content[middle] == value:
                index = middle
                break
            comparisons += 1
            if content[middle] > value:
                right = middle
            else:
                left = middle + 1
        if caching:
            cache[value] = index
        return index, comparisons

    return search


def is_prime(n: int) -> bool:
    """Положительное целое -> признак простоты; для n < 1 — ValueError."""
    if n < 1:
        raise ValueError("Ожидается положительное целое число")
    if n == 1:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


def selection_sort(data: list[int]) -> list[int]:
    """Сортирует копию выбором минимума; исходный список не меняется."""
    result = data.copy()
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        result[start], result[smallest] = result[smallest], result[start]
    return result


def search_experiment() -> list[tuple[int, int, int, int]]:
    """Для N=10,100,1000 возвращает (N, цель, линейные, бинарные сравнения)."""
    rows = []
    for size in (10, 100, 1000):
        data = list(range(size))
        for target in (0, size // 2, size - 1, size):
            linear_index, linear_count = linear_search(data, target)
            binary_index, binary_count = bin_search(data)(target)
            expected = target if target < size else -1
            assert linear_index == binary_index == expected
            rows.append((size, target, linear_count, binary_count))
    return rows


def run_checks() -> None:
    before = measurements.copy()
    assert measurement_summary(measurements) == dict(
        total=144, minimum=7, maximum=21, even=4, count=10, mean=14.4, above_mean=6)
    assert measurement_summary([])["mean"] is None
    assert measurement_summary([-2])["even"] == 1
    assert linear_search(measurements, 18) == (3, 4)
    assert linear_search(measurements, 100) == (-1, 10)
    assert linear_search([], 0) == (-1, 0)
    assert bin_search([])(1) == (-1, 0)
    assert bin_search([1])(1) == (0, 1)
    assert bin_search([1])(2) == (-1, 2)
    assert bin_search([1, 2, 2, 4])(2)[0] in (1, 2)
    cached = bin_search([1, 2, 3], caching=True)
    assert cached(2) == (1, 1)
    assert cached(2) == (1, 0)
    assert cached(9) == (-1, 4)
    assert cached(9) == (-1, 0)
    for n, expected in [(1, False), (2, True), (3, True), (4, False),
                        (25, False), (29, True), (49, False), (97, True)]:
        assert is_prime(n) == expected
    try:
        is_prime(0)
    except ValueError:
        pass
    else:
        raise AssertionError("Неположительное число недопустимо")
    for source, expected in [([], []), ([1], [1]), ([3, 1, 2, 1], [1, 1, 2, 3]),
                             ([0, -2, 4], [-2, 0, 4])]:
        original = source.copy()
        assert selection_sort(source) == expected
        assert source == original
    search_experiment()
    assert measurements == before


def main() -> None:
    run_checks()
    print("Статистика:", measurement_summary(measurements))
    try:
        target = int(input("Число для поиска: "))
    except EOFError:
        target = 18
    index, comparisons = linear_search(measurements, target)
    print(f"Первое вхождение: {index}; сравнений: {comparisons}")
    print("Сортировка выбором:", selection_sort(measurements))
    for number in (1, 2, 25, 29, 49):
        print(f"{number}: простое — {is_prime(number)}")
    print("N | цель | линейный | бинарный")
    for row in search_experiment():
        print(" | ".join(str(value) for value in row))


if __name__ == "__main__":
    main()
