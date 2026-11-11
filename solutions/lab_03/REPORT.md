Лабораторная работа № 3. Алгоритмы, коллекции и функции

---

## Цель работы
Научиться переводить условие задачи в алгоритм, выбирать подходящую структуру данных и разделять программу на небольшие функции с понятными контрактами.

---

## Задачи
- применять условия, циклы и сопоставление с образцом;
- реализовывать поиск, подсчет и накопление;
- работать со списками, кортежами, словарями и множествами;
- выбирать структуру данных с учетом назначения и сложности операций;
- создать функции с позиционными и именованными параметрами;
- использовать аннотации типов и строки документации;
- объяснить области видимости имен по правилу LEGB;
- декомпозировать прикладную задачу на функции;
- оценивать сложность простых алгоритмов.

---

## Задание 1. Условия и классификация данных

### Часть 1-3. 

Программа предназначена для определения уровня результата студента с учетом количества пропущенных
занятий и типа выполненной работы.

В начале программа получает от пользователя три значения: балл, тип работы и количество пропусков.
С помощью конструкции if / elif / else проверяется корректность введенных числовых данных и их
соответствие допустимым диапазонам.

После проверки определяется первоначальный уровень результата: отличный, хороший,
удовлетворительный или недостаточный. Если количество пропусков превышает три, уровень
понижается на одну ступень, при этом он не может опуститься ниже недостаточного.

Для определения текстового обозначения уровня используется последовательность условных 
операторов. Далее с помощью конструкции match / case определяется тип работы: экзаменационная,
проектная или практическая. Также предусмотрена обработка неизвестного типа работы.

В конце программа выводит полученный уровень и пояснение к типу работы.

```python
score = int(input("Введите балл: "))
tipe = input("Введите тип: ").strip()
absences = int(input("Введите количество пропусков: "))

# Часть 1. Проверка диапазонов
if score < 0 or score > 100:
    print("Неправильный ввод балла.")
elif absences < 0 or absences > 5:
    print("Неправильный ввод количества пропусков.")
else:
    # Часть 2. Уровень: 3 - отличный, 2 - хороший, 1 - удовлетворительный, 0 - недостаточный
    if score >= 90:
        level = 3
    elif score >= 75:
        level = 2
    elif score >= 60:
        level = 1
    else:
        level = 0

    if absences > 3 and level > 0:
        level = level - 1

    if level == 3:
        level_name = "отличный"
    elif level == 2:
        level_name = "хороший"
    elif level == 1:
        level_name = "удовлетворительный"
    else:
        level_name = "недостаточный"

    # Часть 3. Тип работы
    match tipe:
        case "exam":
            explanation = "экзаменационная работа"
        case "project":
            explanation = "проектная работа"
        case "practice":
            explanation = "практическая работа"
        case _:
            explanation = "неизвестный тип работы"

    print("Уровень:", level_name)
    print("Тип работы:", explanation)
```
### Часть 4. Тестовые сценарии

Программа проверена на 9 наборах данных. Фактические результаты получены запуском `task_1.py`.

| № | Балл | Тип | Пропуски | Ожидаемый результат | Фактический результат | Статус |
|---|-----:|-----|---------:|---------------------|-----------------------|--------|
| 1 | 0 | exam | 0 | Уровень: недостаточный; Тип работы: экзаменационная работа | Уровень: недостаточный; Тип работы: экзаменационная работа | 
| 2 | 59 | project | 3 | Уровень: недостаточный; Тип работы: проектная работа | Уровень: недостаточный; Тип работы: проектная работа | 
| 3 | 60 | practice | 0 | Уровень: удовлетворительный; Тип работы: практическая работа | Уровень: удовлетворительный; Тип работы: практическая работа | 
| 4 | 74 | exam | 4 | Уровень: недостаточный; Тип работы: экзаменационная работа | Уровень: недостаточный; Тип работы: экзаменационная работа | 
| 5 | 75 | project | 3 | Уровень: хороший; Тип работы: проектная работа | Уровень: хороший; Тип работы: проектная работа | 
| 6 | 89 | practice | 4 | Уровень: удовлетворительный; Тип работы: практическая работа | Уровень: удовлетворительный; Тип работы: практическая работа | 
| 7 | 90 | exam | 0 | Уровень: отличный; Тип работы: экзаменационная работа | Уровень: отличный; Тип работы: экзаменационная работа | 
| 8 | 100 | exam | 5 | Уровень: хороший; Тип работы: экзаменационная работа | Уровень: хороший; Тип работы: экзаменационная работа | 
| 9 | 30 | exam | 5 | Уровень: недостаточный; Тип работы: экзаменационная работа | Уровень: недостаточный; Тип работы: экзаменационная работа | 


#### Порядок проверки условий

1. **Диапазоны.** Сначала проверяется балл (`score < 0 or score > 100`), затем пропуски (`absences < 0 or absences > 5`). Если данные некорректны, выводится сообщение, а классификация не выполняется. Если всё верно, срабатывает `else` с классификацией.
2. **Уровень.** Условия идут от большего порога к меньшему: `>= 90`, `>= 75`, `>= 60`, иначе «недостаточный». Срабатывает первая подходящая ветвь, поэтому нижней границы достаточно. Если проверять в обратном порядке, любой балл от 60 получил бы «удовлетворительный».
3. **Пропуски.** Условие `absences > 3 and level > 0` строгое: 3 пропуска уровень не снижают, а ниже «недостаточного» он не опускается.
4. **Тип работы.** `match / case` сравнивает строку с `exam`, `project`, `practice`. Ветвь `case _` стоит последней.

#### Недостижимые ветви

Полностью недостижимых ветвей нет, каждая сработала хотя бы в одном тесте. Но есть особенности порядка проверок:

- Если и балл, и пропуски некорректны, выводится только сообщение о балле: ветвь проверки пропусков уже не выполняется. 
- Условия `score >= 0` и `score <= 100` в цепочке уровней не нужны: после проверки диапазонов они всегда истинны.
- Ветвь `case _` при корректном вводе не срабатывает, так как по условию тип всегда `exam`, `project` или `practice`. Она нужна только для неизвестного типа (Пример ввода: 50; quiz; 0).

### Практическое расширение

Программа обрабатывает список из 13 записей, проверяет корректность данных, определяет уровень каждого студента с учетом пропусков и типа работы. Результаты сохраняются в список и выводятся отдельно, после чего формируется итоговая сводка с количеством студентов каждого уровня и числом ошибок ввода.

```python
records = [
    (95, "exam", 0),
    (90, "project", 4),
    (82, "practice", 1),
    (75, "exam", 5),
    (74, "project", 0),
    (60, "practice", 3),
    (65, "exam", 4),
    (59, "project", 2),
    (30, "practice", 5),
    (100, "exam", 5),
    (0, "project", 0),
    (88, "quiz", 2),
    (105, "exam", 1),
]


lines = []
count_excellent = 0
count_good = 0
count_satisfactory = 0
count_insufficient = 0
count_errors = 0

for number, (score, tipe, absences) in enumerate(records, start=1):

    # Часть 1. Проверка диапазонов
    if score < 0 or score > 100:
        lines.append(f"Запись {number}: Неправильный ввод балла.")
        count_errors += 1
        continue
    elif absences < 0 or absences > 5:
        lines.append(f"Запись {number}: Неправильный ввод количества пропусков.")
        count_errors += 1
        continue

    # Часть 2. Уровень: 3 - отличный, 2 - хороший, 1 - удовлетворительный, 0 - недостаточный
    if score >= 90:
        level = 3
    elif score >= 75:
        level = 2
    elif score >= 60:
        level = 1
    else:
        level = 0

    if absences > 3 and level > 0:
        level = level - 1

    if level == 3:
        level_name = "отличный"
        count_excellent += 1
    elif level == 2:
        level_name = "хороший"
        count_good += 1
    elif level == 1:
        level_name = "удовлетворительный"
        count_satisfactory += 1
    else:
        level_name = "недостаточный"
        count_insufficient += 1

    # Часть 3. Тип работы
    match tipe:
        case "exam":
            explanation = "экзаменационная работа"
        case "project":
            explanation = "проектная работа"
        case "practice":
            explanation = "практическая работа"
        case _:
            explanation = "неизвестный тип работы"

    lines.append(f"Запись {number}: {score} баллов, {absences} пропусков -> {level_name}, {explanation}")

# После цикла: два блока вывода
print("Индивидуальные результаты:")
for line in lines:
    print(line)

print("\n==Итоговая сводка==\n")
print("отличный:", count_excellent)
print("хороший:", count_good)
print("удовлетворительный:", count_satisfactory)
print("недостаточный:", count_insufficient)
print("ошибки ввода:", count_errors)
print("Всего записей:", len(records))
```

## Задание 2. Циклы и базовые алгоритмические схемы

### Вычисление суммы, минимума, максимума и среднего значения

Программа выполняет обработку списка чисел `measurements` за один проход с помощью цикла
`for`. Вычисляется сумма элементов, находятся минимальное и максимальное значения,
подсчитывается количество чётных чисел. После этого определяется среднее арифметическое 
и отдельным проходом подсчитывается количество элементов, превышающих его. Встроенные функции
`min()`, `max()` и `sum()` не используются.

```python
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
```
### Линейный поиск

Программа запрашивает у пользователя число и выполняет его поиск в списке с помощью линейного
поиска. Элементы проверяются последовательно, начиная с первого. При нахождении совпадения
сохраняется индекс первого вхождения, после чего цикл прекращается с помощью `break`. Если число
отсутствует, программа выводит `-1`.

```python
number = int(input("Введите число для поиска: "))
location = -1

for i in range(len(measurements)):
    if measurements[i] == number:
        location = i
        break

print("Индекс первого вхождения:", location)
```

### Дополнительный алгоритмический эксперимент

Программа запрашивает у пользователя целое число и проверяет, является ли оно простым. Сначала вычисляется квадратный корень числа, после чего проверяются возможные делители от 2 до полученного значения включительно. Если находится делитель без остатка, программа сообщает, что число не является простым. Если делителей не найдено, число признаётся простым. Для чисел меньше 2 предусмотрена отдельная проверка.

```python
number2 = int(input("Введите число для проверки простоты: "))
sq = int(number2**0.5)

if number2 < 2:
    print(f"{number2} - не простое")
elif sq < 2:
    print(f"{number2} - простое")
else:
    for i in range(2, sq + 1):
        if number2 % i == 0:
            print(f"Число не простое, так как делится на {i}")
            break
        elif i == sq:
            print(f"{number2} - простое")
```
#### Оценка временной и пространственной сложности алгоритмов

**1. Вычисление суммы, минимума, максимума и среднего значения**

- **Временная сложность:** `O(n)`, где `n` — количество элементов списка. Первый цикл проходит по всем элементам для вычисления суммы, минимума, максимума и количества чётных чисел. Второй цикл повторно проходит по списку для подсчёта значений больше среднего.
- **Дополнительная память:** `O(1)`, поскольку используются только несколько переменных, количество которых не зависит от размера списка.

**2. Линейный поиск**

- **Временная сложность:** `O(n)`, где `n` — количество элементов списка. В худшем случае необходимо проверить все элементы, если искомое число находится в конце списка или отсутствует.
- **Дополнительная память:** `O(1)`, поскольку используются только переменные для хранения искомого числа и его индекса. Дополнительные коллекции не создаются.

**3. Проверка простоты числа**

- **Временная сложность:** `O(√n)`, где `n` — проверяемое число. Количество проверок зависит от квадратного корня числа, поскольку программа перебирает делители только до этого значения.
- **Дополнительная память:** `O(1)`, поскольку используются только несколько переменных, не зависящих от размера числа.

Ограничение проверки квадратным корнем корректно, поскольку если число имеет делитель больше квадратного корня, то у него обязательно существует парный делитель меньше квадратного корня. Поэтому достаточно проверить делители от 2 до квадратного корня включительно.

### Практическое расширение

#### 1. Сортировка выбором (Selection Sort)

Сортировка выбором последовательно находит минимальный элемент неотсортированной части массива и меняет его местами с первым элементом этой части. На каждой итерации граница отсортированной области увеличивается на один элемент. В результате массив становится упорядоченным по возрастанию.

**Код алгоритма:**

```python
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
```

#### 2. Линейный поиск (Linear Search)

Линейный поиск последовательно проверяет каждый элемент массива, начиная с первого. Если найдено совпадение с искомым числом, алгоритм возвращает индекс элемента и количество выполненных сравнений. Если элемент отсутствует, возвращается индекс `-1`.

**Код алгоритма:**

```python
def linear_search(a, x):
    comparisons = 0

    for i in range(len(a)):
        comparisons += 1

        if a[i] == x:
            return i, comparisons

    return -1, comparisons
```

#### 3. Бинарный поиск (Binary Search)

Бинарный поиск работает только с отсортированным массивом. На каждом шаге алгоритм проверяет средний элемент и сравнивает его с искомым значением. Если значения не совпадают, дальнейший поиск продолжается только в одной половине массива. Таким образом, количество проверяемых элементов значительно сокращается.

**Код алгоритма:**

```python
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
```
#### Весь код

```python
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
```

#### Сравнение количества сравнений

Для эксперимента использовались отсортированные массивы размером 10, 100 и 1000 элементов. В качестве искомого значения выбирался последний элемент массива. Это позволяет рассмотреть случай, когда линейному поиску необходимо проверить все элементы.

| Алгоритм | Выборка | Количество элементов |
|---|---:|---:|
| Линейный поиск | 10 | 10 |
| Бинарный поиск | 10 | 4 |
| Линейный поиск | 100 | 100 |
| Бинарный поиск | 100 | 7 |
| Линейный поиск | 1000 | 1000 |
| Бинарный поиск | 1000 | 10 |

#### Вывод

Линейный поиск имеет временную сложность **O(n)**, поскольку в худшем случае ему приходится
проверять каждый элемент массива. При увеличении размера массива количество сравнений
увеличивается пропорционально количеству элементов.

Бинарный поиск имеет временную сложность **O(log n)**, так как на каждом шаге область
поиска сокращается примерно в два раза. Поэтому даже при значительном увеличении массива
количество сравнений растёт незначительно.

Сортировка выбором имеет временную сложность **O(n²)**, поскольку для каждого элемента
необходимо найти минимальный элемент в оставшейся части массива.

Таким образом, бинарный поиск значительно эффективнее линейного при работе с большими
отсортированными массивами. Однако для его применения предварительно необходимо
отсортировать данные.

## Задание 3. Коллекции и выбор структуры данных

#### 1. Множество всех студентов

Создается множество `set_students`, в которое добавляются имена студентов. Повторяющиеся значения автоматически исключаются.

```python
set_students = set()

for students, labs, attempts in submissions:
    set_students.add(students)

print(set_students)
```

#### 2. Множество всех сданных лабораторных работ

Создается множество `set_labs`, содержащее уникальные идентификаторы лабораторных работ.

```python
set_labs = set()

for students, labs, attempts in submissions:
    set_labs.add(labs)

print(set_labs)
```

#### 3. Словарь попыток каждого студента

Создается словарь `dictionary_attempts`, в котором ключом является имя студента, а значением — список всех его результатов попыток.

```python
dictionary_attempts = {}

for students, labs, attempts in submissions:
    if students not in dictionary_attempts:
        dictionary_attempts[students] = []

    dictionary_attempts[students].append(attempts)

print(dictionary_attempts)
```

#### 4. Словарь лучших результатов

Создается словарь `dictionary_best`, где ключом является кортеж из имени студента и номера лабораторной работы, а значением — лучший результат. Если новая попытка лучше предыдущей, значение обновляется.

```python
dictionary_best = {}

for students, labs, attempts in submissions:
    key = (students, labs)

    if key not in dictionary_best or attempts > dictionary_best[key]:
        dictionary_best[key] = attempts

print(dictionary_best)
```

#### 5. Словарь количества попыток

Создается словарь `attempts_count`, который хранит количество попыток каждого студента по каждой лабораторной работе. Для подсчета используется метод `get()`.

```python
attempts_count = {}

for students, labs, attempts in submissions:
    key = (students, labs)
    attempts_count[key] = attempts_count.get(key, 0) + 1

print(attempts_count)
```

#### 6. Студенты, сдавшие обе лабораторные работы

Создаются два множества: `set_lab1` и `set_lab2`. С помощью операции пересечения `&` находятся студенты, которые присутствуют в обоих множествах.

```python
set_lab1 = set()
set_lab2 = set()

for students, labs, attempts in submissions:
    if labs == "lab_01":
        set_lab1.add(students)
    elif labs == "lab_02":
        set_lab2.add(students)

set_both = set_lab1 & set_lab2

print(set_both)
```

#### 7. Полный код программы

```python
submissions = [
    ("anna", "lab_01", 5),
    ("boris", "lab_01", 4),
    ("anna", "lab_02", 5),
    ("daria", "lab_01", 3),
    ("boris", "lab_02", 5),
    ("anna", "lab_01", 4),
]

set_students = set()
set_labs = set()
dictionary_attempts = {}
dictionary_best = {}
attempts_count = {}

set_lab1 = set()
set_lab2 = set()

for students, labs, attempts in submissions:
    set_students.add(students)
    set_labs.add(labs)

    if students not in dictionary_attempts:
        dictionary_attempts[students] = []
    dictionary_attempts[students].append(attempts)

    key = (students, labs)

    if key not in dictionary_best or attempts > dictionary_best[key]:
        dictionary_best[key] = attempts

    attempts_count[key] = attempts_count.get(key, 0) + 1

    if labs == "lab_01":
        set_lab1.add(students)
    elif labs == "lab_02":
        set_lab2.add(students)

print(set_students)
print(set_labs)
print(dictionary_attempts)
print(dictionary_best)
print(attempts_count)

set_both = set_lab1 & set_lab2
print(set_both)
```
### Обновление структур без полного повторного построения

Для добавления новой записи используется отдельная функция `add_submission()`. Она получает данные одной новой попытки и сразу обновляет все необходимые структуры: множества студентов и лабораторных работ, словари попыток, лучших результатов и количества попыток, а также множества студентов, сдавших каждую лабораторную работу.

Такой подход не требует повторно проходить по всему списку `submissions`: функция обрабатывает только новую запись и вносит соответствующие изменения. Это экономит время и позволяет сохранить уже собранные данные.

```python
def add_submission(student, lab, score):
    set_students.add(student)
    set_labs.add(lab)

    if student not in dictionary_attempts:
        dictionary_attempts[student] = []
    dictionary_attempts[student].append(score)

    key = (student, lab)
    if key not in dictionary_best or score > dictionary_best[key]:
        dictionary_best[key] = score

    attempts_count[key] = attempts_count.get(key, 0) + 1

    if lab == "lab_01":
        set_lab1.add(student)
    elif lab == "lab_02":
        set_lab2.add(student)


add_submission("elena", "lab_01", 5)

set_both = set_lab1 & set_lab2

print(set_students)
print(set_labs)
print(dictionary_attempts)
print(dictionary_best)
print(attempts_count)
print(set_both)
```

### Почему выбраны такие структуры данных

1. **Множество подходит для хранения уникальных значений**, потому что автоматически исключает дубликаты. Повторное добавление одного и того же студента не создаёт новую копию элемента.

2. **Кортеж можно использовать как ключ словаря**, потому что он неизменяемый. Поэтому пара `(student, lab)` может выступать составным ключом.

3. **Список нельзя использовать как ключ словаря**, потому что список изменяемый. Его содержимое может меняться, поэтому он не подходит для использования в качестве ключа.

4. **Словарь предпочтительнее списка для частого поиска результата по составному ключу**, потому что позволяет обращаться к значению напрямую по ключу `(student, lab)`. В списке для поиска пришлось бы последовательно просматривать записи.

### Практическое расширение

В практическом расширении реализован простой командный интерфейс, который позволяет получать информацию из ранее созданных структур данных. Программа работает в цикле и принимает команды пользователя до ввода команды `exit`.

После ввода строка разделяется на команду и её аргументы. С помощью конструкции `match-case` программа определяет, какую операцию необходимо выполнить:

- `student <имя>` — выводит список результатов всех попыток указанного студента;
- `best <имя> <лабораторная>` — выводит лучший результат студента по указанной лабораторной работе;
- `attempts <имя> <лабораторная>` — выводит количество попыток студента по указанной работе;
- `completed <лабораторная>` — выводит множество студентов, у которых есть попытки по указанной лабораторной работе;
- `exit` — завершает работу программы.

Для каждой команды проверяется количество и корректность аргументов. Если данные отсутствуют или команда введена неправильно, программа выводит соответствующее сообщение об ошибке.

Командный интерфейс использует уже заполненные множества и словари. Поэтому для выполнения запросов не требуется заново обрабатывать исходный список записей.

#### Код программы

```python
print()
while True:
    line = input("Введите ваш запрос: ")
    if line == "exit":
        break

    parts = line.split()
    if len(parts) == 0:
        print("ошибка ввода")
        continue

    command = parts[0]
    args = parts[1:]

    match command:
        case "student":
            if len(args) != 1:
                print("ошибка ввода")
            elif args[0] not in dictionary_attempts:
                print("студент не найден")
            else:
                print(dictionary_attempts[args[0]])

        case "best":
            if len(args) != 2:
                print("ошибка ввода")
            elif (args[0], args[1]) not in dictionary_best:
                print("нет данных")
            else:
                print(dictionary_best[(args[0], args[1])])

        case "attempts":
            if len(args) != 2:
                print("ошибка ввода")
            elif (args[0], args[1]) not in attempts_count:
                print("нет данных")
            else:
                print(attempts_count[(args[0], args[1])])

        case "completed":
            if len(args) != 1:
                print("ошибка ввода")
            elif args[0] not in set_labs:
                print("такой работы нет")
            else:
                done = set()
                for student in set_students:
                    if attempts_count.get((student, args[0]), 0) > 0:
                        done.add(student)
                print(done)

        case _:
            print("неизвестная команда")
```

#### Примеры команд

```text
student anna
best anna lab_01
attempts boris lab_02
completed lab_01
exit
```
#### Вывод

```text
Введите ваш запрос: student anna
[5, 5, 4]
Введите ваш запрос: best anna lab_01
5
Введите ваш запрос: attempts boris lab_02
1
Введите ваш запрос: completed lab_01
{'anna', 'daria', 'boris', 'Ivan'}
Введите ваш запрос: exit
```
## Задание 4. Функции, параметры и области видимости

В задании реализованы функции для вычисления среднего значения, нормализации имени, формирования отчёта и очистки списка тегов. Добавлены проверки `assert`, демонстрация позиционных и именованных аргументов, распаковки `*` и `**`, исследование областей видимости LEGB и исправление ошибки изменяемого значения по умолчанию. В практической части реализована передача функций в качестве аргументов и создание замыканий.
```python
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


# Проверки build_report
assert build_report("Анна", [5, 4, 5]) == \
    "Результат: Анна — среднее 4.67, минимум 4, максимум 5, количество 3"
assert build_report("Анна", [5, 4, 5], precision=1, prefix="Итог") == \
    "Итог: Анна — среднее 4.7, минимум 4, максимум 5, количество 3"
assert build_report("Борис", []) == "Результат: Борис — нет результатов"
assert build_report("Анна", [5, 4, 5], precision=0).startswith(
    "Результат: Анна — среднее 5,"
)


# Проверки collect_tags
assert collect_tags("Python", " python ", "") == ("python",)
assert collect_tags("A", "a", lowercase=False) == ("A", "a")
assert collect_tags() == ()
assert collect_tags("  ", "") == ()


# Распаковка списка через * и словаря через **
tag_list = ["Python", "python", "Algo", " "]
print(collect_tags(*tag_list))

options = {"precision": 1, "prefix": "Итог"}
print(build_report("Борис", [4, 3, 5], **options))
```

Функция `arithmetic_mean()` накапливает сумму элементов и делит её на количество элементов. Для пустого списка возвращается `None`. Функция `normalize_name()` разбивает строку на слова, удаляет лишние пробелы и приводит первую букву каждого слова к верхнему регистру.

Функция `build_report()` формирует строку с основными показателями результатов студента. Параметры `precision` и `prefix` объявлены после `*`, поэтому их можно передавать только по имени. Если список результатов пуст, функция сразу возвращает отдельное сообщение.

Функция `collect_tags()` принимает произвольное количество тегов через `*tags`, удаляет пробелы по краям, при необходимости приводит строки к нижнему регистру и исключает пустые и повторяющиеся значения. Множество `seen` используется для проверки повторов, а итог возвращается в виде кортежа.

Вызов `collect_tags(*tag_list)` распаковывает список в отдельные позиционные аргументы. Вызов `build_report(..., **options)` распаковывает словарь в именованные аргументы.

### Исследование LEGB

```python
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
```

LEGB — правило поиска переменных в Python. Имя ищется последовательно в четырёх областях:

1. **Local** — локальная область текущей функции.
2. **Enclosing** — область внешней функции.
3. **Global** — глобальная область модуля.
4. **Built-in** — встроенные имена Python, например `print()` и `len()`.

Схема областей видимости:

```text
┌─ Built-in: print, len, sum, ...
│  ┌─ Global (модуль task_4.py): course, outer, result
│  │  ┌─ Enclosing (функция outer): attempts, inner
│  │  │  ┌─ Local (функция inner): note
│  │  │  └─
│  │  └─
│  └─
└─
```

В функции `inner()` переменная `note` является локальной. Переменная `attempts` находится в объемлющей функции `outer()`, поэтому для её изменения используется `nonlocal`. Имя `course` не найдено в локальной и объемлющей областях, поэтому Python обращается к глобальной области. Встроенные имена, например `print`, ищутся в области Built-in.

После двух вызовов `inner()` значение `attempts` становится равным `2`. Глобальная переменная `course` при этом не изменяется.

### Ошибка изменяемого значения по умолчанию

```python
def add_result_buggy(value, results=[]):
    results.append(value)
    return results


def add_result(value, results=None):
    if results is None:
        results = []
    results.append(value)
    return results


# Демонстрация ошибки
add_result_buggy(1)
second = add_result_buggy(2)
assert second == [1, 2]


# Исправленная версия
add_result(1)
assert add_result(2) == [2]
```

Значение параметра по умолчанию создаётся один раз при определении функции, а не заново при каждом вызове. Поэтому список `results=[]` сохраняется между вызовами `add_result_buggy()`, и новые значения добавляются в один и тот же список.

Исправленный вариант использует `None` в качестве значения по умолчанию. При каждом вызове без переданного списка внутри функции создаётся новый список. Это предотвращает случайное сохранение данных между вызовами.

### Практическое расширение

```python
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

# Именованная функция и lambda
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
```

Функция `apply_to_results()` принимает другую функцию в параметре `operation` и применяет её к каждому элементу последовательности. В примере передаются обычная функция `add_bonus()` и анонимная функция `lambda`, которая переводит результат в долю от 100. Исходный список `scores` не изменяется.

Функция `make_threshold_checker()` создаёт и возвращает вложенную функцию `check()`. Возвращённая функция сравнивает результат с порогом. Значение `threshold` сохраняется в замыкании, поэтому проверки `passed` и `excellent` используют независимые пороги — `60` и `90`.

### Ответы на вопросы и вывод

- **Зачем нужен `nonlocal`?** Он позволяет изменять переменную из объемлющей функции, не создавая локальную переменную с тем же именем.
- **В каком порядке Python ищет имена?** Local → Enclosing → Global → Built-in.
- **Почему нельзя использовать изменяемый список как значение по умолчанию?** Он создаётся один раз и может сохранять изменения между вызовами функции.
- **Что такое замыкание?** Это функция, которая сохраняет доступ к переменным из области, в которой была создана.
- **Что демонстрирует `lambda`?** Создание небольшой анонимной функции, которую можно передать как аргумент.


## Задание 5. Анализатор учебных результатов

### Описание функций

Программа разделена на функции, каждая из которых выполняет отдельную задачу:

- `mean(values)` — вычисляет среднее арифметическое результатов.
- `minimum(values)` — находит минимальный результат без использования `min()`.
- `maximum(values)` — находит максимальный результат без использования `max()`.
- `classify(score)` — определяет категорию студента по среднему баллу.
- `student_summary(name, results)` — формирует словарь со статистикой одного студента.
- `find_top_students(students)` — находит студента или студентов с наибольшим средним баллом.
- `group_summary(students)` — вычисляет общую статистику группы и количество студентов в каждой категории.
- `make_rating(students)` — формирует рейтинг студентов по среднему баллу. Студенты без результатов помещаются в конец.
- `fmt(value)` — форматирует числовые значения для вывода, а при отсутствии данных возвращает прочерк.
- `format_report(student_data, group_data)` — формирует итоговый текстовый отчет.
- `run(data)` — объединяет основные этапы работы программы и возвращает готовый отчет.

```python
students = {
    "Анна": [78, 91, 84, 88],
    "Борис": [60, 72, 68],
    "Дарья": [95, 93, 97, 90],
    "Илья": [55, 61],
}

CATEGORIES = ("отличный", "хороший", "удовлетворительный", "недостаточный", "нет данных")


def mean(values):
    if not values:
        return None
    total = 0
    for value in values:
        total += value
    return total / len(values)


def minimum(values):
    if not values:
        return None
    result = values[0]
    for value in values:
        if value < result:
            result = value
    return result


def maximum(values):
    if not values:
        return None
    result = values[0]
    for value in values:
        if value > result:
            result = value
    return result


def classify(score):
    if score is None:
        return "нет данных"
    if score >= 90:
        return "отличный"
    if score >= 75:
        return "хороший"
    if score >= 60:
        return "удовлетворительный"
    return "недостаточный"


def student_summary(name, results):
    average = mean(results)
    return {
        "name": name,
        "count": len(results),
        "mean": average,
        "min": minimum(results),
        "max": maximum(results),
        "category": classify(average),
    }


def find_top_students(students):
    best = None
    top = []
    for name, results in students.items():
        average = mean(results)
        if average is None:
            continue
        average = round(average, 6)
        if best is None or average > best:
            best = average
            top = [name]
        elif average == best:
            top.append(name)
    return top


def group_summary(students):
    total = 0
    count = 0
    categories = {}
    for category in CATEGORIES:
        categories[category] = 0

    for results in students.values():
        for value in results:
            total += value
            count += 1
        categories[classify(mean(results))] += 1

    return {
        "students_count": len(students),
        "results_count": count,
        "group_mean": total / count if count else None,
        "categories": categories,
        "top": find_top_students(students),
    }


def make_rating(students):
    with_data = []
    without_data = []
    for name, results in students.items():
        summary = student_summary(name, results)
        if summary["mean"] is None:
            without_data.append(summary)
        else:
            with_data.append(summary)
    with_data = sorted(with_data, key=lambda item: item["mean"], reverse=True)
    return with_data + without_data


def fmt(value):
    if value is None:
        return "—"
    return f"{value:.2f}"


def format_report(student_data, group_data):
    lines = ["РЕЙТИНГ СТУДЕНТОВ"]
    if not student_data:
        lines.append("  студентов нет")
    for place, item in enumerate(student_data, start=1):
        lines.append(
            f"  {place}. {item['name']}: среднее {fmt(item['mean'])}, "
            f"мин {fmt(item['min'])}, макс {fmt(item['max'])}, "
            f"категория: {item['category']}"
        )

    lines.append("")
    lines.append("СВОДКА ПО ГРУППЕ")
    lines.append(f"  Студентов: {group_data['students_count']}")
    lines.append(f"  Общий средний результат: {fmt(group_data['group_mean'])}")
    if group_data["top"]:
        lines.append("  Лидер(ы): " + ", ".join(group_data["top"]))
    else:
        lines.append("  Лидер(ы): нет")
    lines.append("  По категориям:")
    for category, number in group_data["categories"].items():
        lines.append(f"    {category}: {number}")
    return "\n".join(lines)


def run(data):
    return format_report(make_rating(data), group_summary(data))


# сценарии проверки

# 1. обычный набор данных
copy_before = {name: list(results) for name, results in students.items()}
rating = make_rating(students)
assert [item["name"] for item in rating] == ["Дарья", "Анна", "Борис", "Илья"]
assert group_summary(students)["top"] == ["Дарья"]
assert group_summary(students)["categories"]["отличный"] == 1
assert students == copy_before  # исходные данные не изменены

# 2. один студент
single = {"Олег": [80, 90]}
assert group_summary(single)["top"] == ["Олег"]
assert group_summary(single)["group_mean"] == 85
assert student_summary("Олег", [80, 90])["category"] == "хороший"

# 3. несколько лидеров
tie = {"А": [90, 80], "Б": [85, 85], "В": [50]}
assert group_summary(tie)["top"] == ["А", "Б"]

# 4. пустая группа
empty = {}
empty_summary = group_summary(empty)
assert empty_summary["students_count"] == 0
assert empty_summary["group_mean"] is None
assert empty_summary["top"] == []
assert "студентов нет" in run(empty)

# 5. студент без результатов
with_empty = {"Аня": [70, 80], "Пусто": []}
item = student_summary("Пусто", [])
assert item["mean"] is None and item["min"] is None and item["max"] is None
assert item["category"] == "нет данных"
assert group_summary(with_empty)["top"] == ["Аня"]
assert group_summary(with_empty)["group_mean"] == 75
assert make_rating(with_empty)[-1]["name"] == "Пусто"

# 6. граничные значения категорий
assert classify(59) == "недостаточный"
assert classify(60) == "удовлетворительный"
assert classify(74) == "удовлетворительный"
assert classify(75) == "хороший"
assert classify(89) == "хороший"
assert classify(90) == "отличный"
assert classify(100) == "отличный"
assert classify(0) == "недостаточный"

# минимум и максимум
assert minimum([5, 3, 9]) == 3
assert maximum([5, 3, 9]) == 9
assert minimum([]) is None and maximum([]) is None

# вывод
print(run(students))
print("\nВсе проверки пройдены")

```

### Контракты публичных функций

Контракт определяет допустимые входные данные, результат работы функции и особенности её выполнения.

| Функция | Входные данные | Результат и особые случаи |
|---|---|---|
| `mean(values)` | Список чисел | Среднее арифметическое. Для пустого списка возвращает `None`. |
| `minimum(values)` | Список чисел | Минимальное значение. Для пустого списка возвращает `None`. |
| `maximum(values)` | Список чисел | Максимальное значение. Для пустого списка возвращает `None`. |
| `classify(score)` | Число от 0 до 100 или `None` | Возвращает категорию результата. При `None` возвращает «нет данных». |
| `student_summary(name, results)` | Строка с именем и список результатов | Словарь с количеством результатов, средним, минимумом, максимумом и категорией. Для пустого списка числовые показатели равны `None`. |
| `find_top_students(students)` | Словарь студентов и списков результатов | Список лидеров. При отсутствии результатов возвращает пустой список. При равенстве средних включает всех лидеров. |
| `group_summary(students)` | Словарь студентов и их результатов | Словарь с общей статистикой группы. Для пустой группы средний балл равен `None`, список лидеров пуст. |
| `make_rating(students)` | Словарь студентов и их результатов | Отсортированный список статистики студентов. Студенты без результатов находятся в конце. |
| `fmt(value)` | Число или `None` | Строка с числом, округленным до двух знаков, либо прочерк. |
| `format_report(student_data, group_data)` | Список статистики студентов и словарь статистики группы | Готовый текстовый отчет. При отсутствии студентов выводится соответствующее сообщение. |
| `run(data)` | Словарь исходных данных группы | Возвращает полный текстовый отчет. Для пустой группы формирует отчет без ошибок. |

*Примечание: функции рассчитаны на корректные входные типы данных и не выполняют отдельную проверку некорректных типов или значений.*

### Декомпозиция программы

Программа разделена на три основных этапа:

1. **Вычисление статистики.** Функции `mean()`, `minimum()` и `maximum()` выполняют базовые вычисления, а `classify()` определяет категорию результата.
2. **Анализ данных.** Функции `student_summary()`, `find_top_students()`, `group_summary()` и `make_rating()` формируют индивидуальную и общую статистику, а также рейтинг студентов.
3. **Формирование отчета.** Функции `fmt()` и `format_report()` отвечают за форматирование результатов, а `run()` объединяет все этапы.

Такое разделение упрощает чтение и проверку программы, позволяет повторно использовать функции и изменять отдельные части без необходимости переписывать весь код.

### Оценка сложности

Обозначим:

- `N` — количество студентов;
- `R` — общее количество оценок всех студентов;
- `K` — количество оценок конкретного студента.

| Функция | Временная сложность |
|---|---|
| `mean()` | `O(K)` |
| `minimum()` | `O(K)` |
| `maximum()` | `O(K)` |
| `classify()` | `O(1)` |
| `student_summary()` | `O(K)` |
| `find_top_students()` | `O(N + R)` |
| `group_summary()` | `O(N + R)` |
| `make_rating()` | `O(R + N log N)` |
| `fmt()` | `O(1)` |
| `format_report()` | `O(N)` |
| `run()` | `O(R + N log N)` |

**Сложность построения общей статистики** составляет `O(N + R)`, поскольку программа проходит по студентам и их оценкам, накапливает сумму, подсчитывает результаты и определяет категории.

Общая временная сложность выполнения программы составляет `O(R + N log N)`, поскольку дополнительно выполняется сортировка рейтинга студентов.

Дополнительная память составляет `O(N)` для хранения сформированной статистики, рейтинга и списка лидеров. Исходный словарь студентов при этом не изменяется.

### Проверка программы

Для проверки были подготовлены следующие сценарии:

1. Обычный набор данных — проверка формирования рейтинга и общей статистики.
2. Один студент — проверка работы с группой из одной записи.
3. Несколько лидеров — проверка одинаковых средних результатов.
4. Пустая группа — проверка отсутствия студентов.
5. Студент без результатов — проверка обработки пустого списка оценок.
6. Граничные значения — проверка правильного определения категорий.

Дополнительно проверены функции поиска минимума и максимума, включая пустые списки.

Для проверки использованы утверждения `assert`. После успешного выполнения всех проверок программа выводит сообщение `Все проверки пройдены`.
