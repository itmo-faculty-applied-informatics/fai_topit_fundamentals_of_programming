import copy
import gc
import sys
import tracemalloc

results = []

#Сценарий со списком из 100000 чисел
tracemalloc.start()
numbers = list(range(100_000))
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
results.append({
    "name": "list(range(100000))",
    "count": len(numbers),
    "size": sys.getsizeof(numbers),
    "current": current,
    "peak": peak
})
del numbers

#Сценарий range(100000)
tracemalloc.start()
numbers = range(100_000)
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
results.append({
    "name": "range(100000)",
    "count": len(numbers),
    "size": sys.getsizeof(numbers),
    "current": current,
    "peak": peak
})

print("ОТЧЁТ О ПОТРЕБЛЕНИИ ПАМЯТИ")
for result in results:
    print(f'\nСценарий: {result["name"]}')
    print(f'Количество элементов: {result["count"]}')
    print(f'Размер внешнего объекта: {result["size"]/2**10:.2f} КБ')
    print(f'Текущая память: {result["current"]/2**10:.2f} КБ')
    print(f'Пиковая память: {result["peak"]/2**10:.2f} КБ')

# Сравнение пиковой памяти
list_peak = results[0]["peak"]
range_peak = results[1]["peak"]
print(f'\nОтношение пиковой памяти list/range: {(list_peak / range_peak):.2f}')