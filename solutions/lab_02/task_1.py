# Эксперимент А. Неизменяемый объект
a = 10
b = a

print(a, b)
print(id(a), id(b))

a += 1

print(a, b)
print(id(a), id(b))

# Эксперимент В. Изменяемый объект
first = [10, 20]
second = first
print(first, second)
print(id(first), id(second))
second.append(30)
print(first, second)
print(id(first), id(second))
second = [10, 20, 30]
print(first, second)
print(first == second)
print(first is second)
second.append(40)
print(first, second)

# Практическая задача

config1 = ["Проект", ["Петр","Иван"],[8080, 0]]
# Создание с помощью присваивание
config2 = config1

print("До изменений:")
print("config1 =", config1)
print("config2 =", config2)

config2[1].append("Пётр")
config2[2][0] = 9000

print("\nПосле изменения config2:")
print("config1 =", config1)
print("config2 =", config2)

# Создание независимой конфигурации
config3 = ["Проект", ["Петр","Иван"],[8080, 0]]
config1[1].append("Мария")
config1[2][0] = 9000
assert config1 is not config3
assert config1[1] is not config3[1]
assert config1[2] is not config3[2]

assert "Мария" not in config3[1]
assert config1[2][0] == 9000
assert config3[2][0] == 8080
print("\nПервая конфигурация (зависимая с сonfig2):", config1)
print("Вторая (независимая)конфигурация:", config3)
