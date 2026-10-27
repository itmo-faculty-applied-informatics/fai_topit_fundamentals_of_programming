import sys

# Часть 1. Размер отдельных объектов

empty_list = []
numbers_list = list(range(10))
numbers_tuple = tuple(range(10))
text = "abcdefghij"
number = 100
empty_value = None

print("Размер пустого списка:", sys.getsizeof(empty_list), "байт")
print("Размер списка из 10 чисел:", sys.getsizeof(numbers_list), "байт")
print("Размер кортежа из 10 чисел:", sys.getsizeof(numbers_tuple), "байт")
print("Размер строки из 10 символов:", sys.getsizeof(text), "байт")
print("Размер целого числа:", sys.getsizeof(number), "байт")
print("Размер None:", sys.getsizeof(empty_value), "байт")

# Часть 2. Рост списка

growth_list = []
previous_size = sys.getsizeof(growth_list)

print("Начальное состояние: длина =", len(growth_list), "размер =", previous_size, "байт")

for i in range(100):
    growth_list.append(i)
    current_size = sys.getsizeof(growth_list)

    if current_size != previous_size:
        print("Длина =", len(growth_list),
              "размер =", current_size, "байт")
        previous_size = current_size

# Часть 3. Измерение через tracemalloc

import tracemalloc

# Вариант 1: список из 100 000 чисел

tracemalloc.start()

numbers = list(range(100_000))

current, peak = tracemalloc.get_traced_memory()

print("list(range(100_000)):")
print("Текущая память:", current / 1024, "КБ")
print("Пиковая память:", peak / 1024, "КБ")

tracemalloc.stop()

# Вариант 2: объект range


tracemalloc.start()

numbers = range(100_000)

current, peak = tracemalloc.get_traced_memory()

print("\nrange(100_000):")
print("Текущая память:", current / 1024, "КБ")
print("Пиковая память:", peak / 1024, "КБ")

tracemalloc.stop()