import gc

first = []
second = []

first.append(second)
second.append(first)

print("first ссылается на second:", first[0] is second)
print("second ссылается на first:", second[0] is first)

print("Автоматическая сборка включена:", gc.isenabled())
print("Пороги сборщика:", gc.get_threshold())
print("Статистика поколений:", gc.get_stats())

# Сохранение идентификатора списков
first_id = id(first)
second_id = id(second)

print("Идентификатор first:", first_id)
print("Идентификатор second:", second_id)

# Удаляние имени ссылок
del first
del second

# Запуск сборщика мусора
collected = gc.collect()

print("Количество собранных объектов:", collected)

# Дополнительный эксперимент

gc.disable()

print("\nОтключение автоматического сборщика мусора")
print("Проверка отключен ли сборщик мусора ", gc.isenabled())

cycle1 = []
cycle2 = []
cycle3 = []
cycle4 = []

cycle1.append(cycle2)
cycle2.append(cycle1)

cycle3.append(cycle4)
cycle4.append(cycle3)

del cycle1, cycle2, cycle3, cycle4

collected2 = gc.collect()

print("\nВключение сборщика вручную мусора")
print("Собранные объекты: ", collected2)

gc.enable()

print("\nВключение автоматического сборщика мусора")
print("Проверка включен ли сборщик мусора ", gc.isenabled())


# Практическая задача

before = gc.collect()
print("Собрано объектов до создания графа:", before)

node_1 = {"name": "1", "links": []}
node_2 = {"name": "2", "links": []}
node_3 = {"name": "3", "links": []}

node_1["links"].append(node_2)
node_2["links"].append(node_3)
node_3["links"].append(node_1)

node_4 = {"name": "4", "links": []}

# Вывод связей графа
print("\nСвязи графа:")
print("1 ->", node_1["links"][0]["name"])
print("2 ->", node_2["links"][0]["name"])
print("3 ->", node_3["links"][0]["name"])
print("4 -> независимый узел")



# Удаление внешних имен
del node_1, node_2, node_3


collected = gc.collect()
print("\nСобрано объектов после удаления цикла:", collected)

# Проверка независимого узла
print("Независимый узел доступен:", node_4["name"] == "4")
print("Узел 4:", node_4)

