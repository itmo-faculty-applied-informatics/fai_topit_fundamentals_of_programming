import sys

data = [1, 2, 3]
print("После создания:", sys.getrefcount(data))

alias = data
print("После создания alias:", sys.getrefcount(data))

container = [data]
print("После помещения в контейнер:", sys.getrefcount(data))

del alias
print("После del alias:", sys.getrefcount(data))

container.clear()
print("После очистки контейнера:", sys.getrefcount(data))

import weakref


class Record:
    pass


record = Record()
weak_record = weakref.ref(record)

print(weak_record())
del record
print(weak_record())

# Практическая задача

import weakref

cache = weakref.WeakValueDictionary()

class Record:
    pass

record1 = Record()
record2 = Record()
record3 = Record()

cache["key1"] = record1
cache["key2"] = record2
cache["key3"] = record3

print("Реестр:")

for key, obj in cache.items():
    print(f"Ключ: {key} -> {obj}")

del record3

print("\nПосле удаления одной сильной ссылки (record3)")

for key, obj in cache.items():
    print(f"Ключ: {key} -> {obj}")

del record2

print("\nПосле удаления двух сильных ссылок (record2)")

for key, obj in cache.items():
    print(f"Ключ: {key} -> {obj}")


