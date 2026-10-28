import gc

first = []
second = []

first.append(second)
second.append(first)

print("first ссылается на second:", first[0] is second)
print("second ссылается на first:", second[0] is first)

print(f"Сборщик включён:      {gc.isenabled()}")
print(f"Пороги поколений:     {gc.get_threshold()}")
print(f"Статистика поколений: {gc.get_count()}")

id1, id2 = id(first), id(second)
del first
del second

collected_after_del = gc.collect()
print(f"Объектов собрано после del first/second:  {collected_after_del}")
print('===============ЭКСПЕРИМЕНТ==============')
#ЭКСПЕРИМЕНТ
gc.disable()
print(f"Сборщик отключён: {not gc.isenabled()}")
cycles = []

for i in range(5):
    c = [f"cycle_{i}_c"]
    d = [f"cycle_{i}_d"]
    c.append(d)
    d.append(c)
    cycles.append(c)

print(f"Создано 5 циклов. Счётчики поколений: {gc.get_count()}")
del cycles
collected_manual = gc.collect()
print(f"Ручной сборщик собрал объектов: {collected_manual}")
print(f"Счётчики поколений после сборки:     {gc.get_count()}")

gc.enable()
print(f"Сборщик восстановлен: {gc.isenabled()}")

print('===============ПРАКТИЧЕСКАЯ ЗАДАЧА==============')
node_a = {"name": "A", "neighbors": []}
node_b = {"name": "B", "neighbors": []}
node_c = {"name": "C", "neighbors": []}
node_d = {"name": "D", "neighbors": []}

node_a["neighbors"].append(node_b)
node_b["neighbors"].append(node_c)
node_c["neighbors"].append(node_a)


id_d = id(node_d)

print("\n[ Связи графа ]")
print(f"  {node_a['name']} => {[n['name'] for n in node_a['neighbors']]}")
print(f"  {node_b['name']} => {[n['name'] for n in node_b['neighbors']]}")
print(f"  {node_c['name']} => {[n['name'] for n in node_c['neighbors']]}")
print(f"  {node_d['name']} => {[n['name'] for n in node_d['neighbors']]} (независим)")

gc.collect()
baseline = 0

del node_a
del node_b
del node_c

print(f"\n[ Проверка независимого узла D ]")
print(f"  node_d доступен: {node_d}")
print(f"  id(node_d) == {id_d}: {id(node_d) == id_d}")

collected = gc.collect()
print(f"\n[ Ручной gc.collect() ]")
print(f"  Собрано объектов: {collected}")

print(f"\n[ Итог ]")
print(f"  Объектов собрано: {collected - baseline}")
print(f"  Узел D продолжает существовать: {node_d['name']}")