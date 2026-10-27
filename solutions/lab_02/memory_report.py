import sys
import tracemalloc

def measure(name, kind, count):
    tracemalloc.start()

    if kind == "empty_list":
        obj = []
    elif kind == "list10":
        obj = list(range(10))
    elif kind == "tuple10":
        obj = tuple(range(10))
    elif kind == "string":
        obj = "abcdefghij"
    elif kind == "integer":
        obj = 100
    elif kind == "none":
        obj = None
    elif kind == "list100":
        obj = list(range(100))
    elif kind == "big_list":
        obj = list(range(100_000))
    elif kind == "range":
        obj = range(100_000)

    size = sys.getsizeof(obj)
    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    result = {
        "name": name,
        "count": count,
        "size": size,
        "current": current,
        "peak": peak
    }

    return result


results = []

results.append(measure("Пустой список", "empty_list", 0))
results.append(measure("Список из 10 чисел", "list10", 10))
results.append(measure("Кортеж из 10 чисел", "tuple10", 10))
results.append(measure("Строка из 10 символов", "string", 10))
results.append(measure("Целое число", "integer", 1))
results.append(measure("None", "none", 0))
results.append(measure("Список из 100 чисел", "list100", 100))
results.append(measure("Список из 100000 чисел", "big_list", 100000))
results.append(measure("range из 100000 чисел", "range", 100000))


print("ОТЧЁТ О ПОТРЕБЛЕНИИ ПАМЯТИ")

for result in results:
    print("\nСценарий:", result["name"])
    print("Количество элементов:", result["count"])
    print("Размер объекта:", result["size"], "байт")
    print("Текущая память:", round(result["current"] / 1024, 2), "КБ")
    print("Пиковая память:", round(result["peak"] / 1024, 2), "КБ")


list_peak = results[7]["peak"]
range_peak = results[8]["peak"]

print("\nСРАВНЕНИЕ СПИСКА И RANGE")

if range_peak > 0:
    ratio = list_peak / range_peak
    print("Пиковая память списка больше в", round(ratio, 2), "раз")