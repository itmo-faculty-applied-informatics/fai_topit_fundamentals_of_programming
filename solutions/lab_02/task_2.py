import copy

# Функция для вывода содержимого всех списков
def status(original, alias, shallow, deep):
    print("original =", original)
    print("alias    =", alias)
    print("shallow  =", shallow)
    print("deep     =", deep)


# Функция для вывода идентификаторов внешних списков
def status_id(original, alias, shallow, deep):
    print("original:", id(original))
    print("alias:", id(alias))
    print("shallow:", id(shallow))

    print("deep:", id(deep))


# Функция для вывода идентификаторов первых вложенных списков
def status_id_nested_lists(original, alias, shallow, deep):
    print("original:", id(original[0]))
    print("alias:", id(alias[0]))
    print("shallow:", id(shallow[0]))
    print("deep:", id(deep[0]))


# Функция для вывода идентификаторов первых оценок
def status_id_first_grades(original, alias, shallow, deep):
    print("original:", id(original[0][1]))
    print("alias:", id(alias[0][1]))
    print("shallow:", id(shallow[0][1]))
    print("deep:", id(deep[0][1]))


# Создание исходного списка
original = [
    ["Python", 5],
    ["Algorithms", 4]
]

# Создание трех вариантов
alias = original
shallow = original.copy()
deep = copy.deepcopy(original)


# Состояние до изменений
print("=== До изменений ===")
status(original, alias, shallow, deep)

print("\nИдентификаторы внешних списков:")
status_id(original, alias, shallow, deep)

print("\nИдентификаторы первых вложенных списков:")
status_id_nested_lists(original, alias, shallow, deep)

print("\nИдентификаторы первых оценок:")
status_id_first_grades(original, alias, shallow, deep)


# Первое изменение
original.append(["Databases", 5])

print("\n=== После добавления Databases ===")
status(original, alias, shallow, deep)

print("\nИдентификаторы внешних списков:")
status_id(original, alias, shallow, deep)

print("\nИдентификаторы первых вложенных списков:")
status_id_nested_lists(original, alias, shallow, deep)

print("\nИдентификаторы первых оценок:")
status_id_first_grades(original, alias, shallow, deep)


# Второе изменение
original[0][1] = 3

print("\n=== После изменения оценки Python ===")
status(original, alias, shallow, deep)

print("\nИдентификаторы внешних списков:")
status_id(original, alias, shallow, deep)

print("\nИдентификаторы первых вложенных списков:")
status_id_nested_lists(original, alias, shallow, deep)

print("\nИдентификаторы первых оценок:")
status_id_first_grades(original, alias, shallow, deep)

# Ошибочное создание матрицы
wrong_matrix = [[0] * 3] * 3

wrong_matrix[0][0] = 1

print("wrong_matrix =", wrong_matrix)

print("Идентификаторы строк:")
print(id(wrong_matrix[0]))
print(id(wrong_matrix[1]))
print(id(wrong_matrix[2]))


# Правильное создание матрицы
correct_matrix = [[0] * 3 for _ in range(3)]

correct_matrix[0][0] = 1

print("\ncorrect_matrix =", correct_matrix)

print("Идентификаторы строк:")
print(id(correct_matrix[0]))
print(id(correct_matrix[1]))
print(id(correct_matrix[2]))
