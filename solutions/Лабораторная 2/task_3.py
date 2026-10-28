import sys
import weakref

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

print('-------------------------------------')

class Record:
    pass

record = Record()
weak_record = weakref.ref(record)

print(weak_record())
del record
print(weak_record())

print('\n--------ПРАКТИЧЕСКАЯ ЗАДАЧА---------')

class Record:
    pass

registry = weakref.WeakValueDictionary()

rec1 = Record()
rec1.name = "rec1"
rec2 = Record()
rec2.name = "rec2"
rec3 = Record()
rec3.name = "rec3"

registry["1"] = rec1
registry["2"] = rec2
registry["3"] = rec3

print("После регистрации всех трёх:", sorted(registry.keys()))

del rec3
print("После del rec3:", sorted(registry.keys()))

del rec2
print("После del rec2:", sorted(registry.keys()))

print("rec1 жива:", registry["1"] is rec1)

del rec1
print("После del rec1:", sorted(registry.keys()))