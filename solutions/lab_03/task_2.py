measurements = [12, 15, 11, 18, 18, 9, 21, 15, 7, 18]

summa = 0
smallest = measurements[0]
largest = measurements[0]
count_ch = 0

for i in measurements:
    summa = summa + i
    if i < smallest:
        smallest = i
    if i > largest:
        largest = i
    if i % 2 == 0:
        count_ch += 1


arithmetic_mean = summa / len(measurements)

count_ar = 0
for i in measurements:
    if i > arithmetic_mean:
        count_ar += 1

print("Сумма:", summa)
print("Минимум:", smallest)
print("Максимум:", largest)
print("Количество чётных:", count_ch)
print("Среднее арифметическое:", arithmetic_mean)
print("Количество значений больше среднего:", count_ar)


# Линейный поиск
number = int(input("Введите число для поиска: "))
location = -1  # по умолчанию «не найдено»
for i in range(len(measurements)):
    if measurements[i] == number:
        location = i
        break
print("Индекс первого вхождения:", location)

# Дополнительный алгоритмический эксперимент

number2 = int(input("Введите число для проверки простоты: "))
sq = int(number2**0.5)
if number2 < 2:
    print(f"{number2} - не простое")
elif sq < 2:
    print(f"{number2} - простое")
else:
    for i in range(2,sq+1):
        if number2 % i ==0 :
            print(f"Число не простое, так как делится на {i}")
            break
        elif i == sq:
            print(f"{number2} - простое")

# Практическое расширение

array = [
    47, 183, 92, 15, 126, 78, 164, 33, 109, 58,
    141, 7, 195, 82, 66, 120, 29, 173, 99, 52,
    134, 21, 160, 88, 3, 117, 70, 188, 41, 105,
    152, 61, 25, 178, 94, 12, 139, 84, 56, 197,
    113, 38, 168, 75, 9, 146, 101, 64, 181, 27,
    123, 50, 157, 90, 17, 135, 72, 192, 44, 108,
    166, 31, 86, 129, 5, 149, 59, 176, 97, 23,
    115, 68, 185, 40, 154, 80, 13, 131, 102, 171,
    36, 144, 77, 199, 54, 119, 91, 20, 162, 63,
    137, 48, 107, 175, 10, 124, 85, 158, 34, 190,
]


def selection_sort(values):
    A = values[:]
    n = len(A)
    for j in range(n - 1):
        smallest = j
        for i in range(j + 1, n):
            if A[i] < A[smallest]:
                smallest = i
        A[j], A[smallest] = A[smallest], A[j]
    return A


def linear_search(a, x):
    comparisons = 0
    for i in range(len(a)):
        comparisons += 1
        if a[i] == x:
            return i, comparisons
    return -1, comparisons


def binary_search(a, x):
    comparisons = 0
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if a[mid] == x:
            return mid, comparisons
        elif a[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comparisons


x = int(input("Какое число надо найти: "))

sorted_array = selection_sort(array)
lin_index, lin_comparisons = linear_search(sorted_array, x)
bin_index, bin_comparisons = binary_search(sorted_array, x)

print("Отсортированный массив:", sorted_array)
print("Линейный поиск: индекс =", lin_index, ", сравнений =", lin_comparisons)
print("Бинарный поиск: индекс =", bin_index, ", сравнений =", bin_comparisons)