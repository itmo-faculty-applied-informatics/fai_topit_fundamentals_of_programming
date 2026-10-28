import sys
import tracemalloc

print('----------ЧАСТЬ 1. РАЗМЕР ОТДЕЛЬНЫХ ОБЪЕКТОВ----------')
empty_list = []
list_10 = list(range(10))
tuple_10 = tuple(range(10))
str_10 = '0123456789'
intx = 67
no = None

print(f"Пустой список:              {sys.getsizeof(empty_list)} байт")
print(f"Список из 10 целых:         {sys.getsizeof(list_10)} байт")
print(f"Кортеж из 10 целых:         {sys.getsizeof(tuple_10)} байт")
print(f"Строка из 10 символов:      {sys.getsizeof(str_10)} байт")
print(f"Целое число:                {sys.getsizeof(intx)} байт")
print(f"Объект None:                {sys.getsizeof(no)} байт")

print('\n')
print('----------ЧАСТЬ 2. РОСТ СПИСКА----------')
sp = []
size0 = sys.getsizeof(sp)
for i in range(100):
    sp.append(i)
    cur_size = sys.getsizeof(sp)
    if cur_size != size0:
        print(f'Длина списка: {len(sp)}, размер: {cur_size}')
        size0 = cur_size
print('\n')
print('----------ЧАСТЬ 3. ИЗМЕРЕНИЕ ЧЕРЕЗ tracemalloc----------')
#exp 1
tracemalloc.start()
numbers = list(range(100_000))
current_list, peak_list = tracemalloc.get_traced_memory()
tracemalloc.stop()
print("list(range(100_000))")
print(f"  Текущая память: {current_list / 1024:.2f} КБ")
print(f"  Пиковая память: {peak_list / 1024:.2f} КБ")

#exp 2
tracemalloc.start()
numbers = range(100_000)
current_list, peak_list = tracemalloc.get_traced_memory()
tracemalloc.stop()
print("range(100_000)")
print(f"  Текущая память: {current_list / 1024:.2f} КБ")
print(f"  Пиковая память: {peak_list / 1024:.2f} КБ")

