import copy

#Эксперимент A. Неизменяемый объект
a = 10
b = a
print(a, b)
print(id(a), id(b))
a += 1
print(a, b)
print(id(a), id(b))

print('-----------------')
#Эксперимент B. Изменяемый объект
first = [10, 20]
second = first
print(first, second)
print(id(first), id(second))
second.append(30)
print(first, second)
print(id(first), id(second))

print('-----------------')
#Дополнение по заданию
second = [10, 20, 30]
print(f'second == first: {second == first}')
print(f'second is first: {second is first}')
second.append(40)
print(first)

print('--------ПРАКТИЧЕСКАЯ ЗАДАЧА---------')

config_1 = {
    "name": "Task Tracker v1.0",
    "participants": ["Иванов", "Петров"],
    "launch_params": {
        "host": "localhost",
        "port": 8080,
        "debug": False
    },
}

config_2_shallow = config_1

print("До изменений:")
print(f"  config_1: {config_1}")
print(f"  config_2: {config_2_shallow}\n")

config_2_shallow["name"] = "Task Tracker v2.0"
config_2_shallow["participants"].append("Сидоров")
config_2_shallow["launch_params"]["port"] = 9090
config_2_shallow["launch_params"]["debug"] = True

print("После изменений в config_2 (простое присваивание):")
print(f"  config_1: {config_1}")
print(f"  config_2: {config_2_shallow}\n")

config_1 = {
    "name": "Task Tracker v1.0",
    "participants": ["Иванов", "Петров"],
    "launch_params": {
        "host": "localhost",
        "port": 8080,
        "debug": False
    },
}

config_2_independent = copy.deepcopy(config_1)

print("До изменений (deepcopy):")
print(f"  config_1: {config_1}")
print(f"  config_2: {config_2_independent}\n")

config_2_independent["name"] = "Task Tracker v2.0"
config_2_independent["participants"].append("Сидоров")
config_2_independent["launch_params"]["port"] = 9090
config_2_independent["launch_params"]["debug"] = True

print("После изменений в config_2 (deepcopy):")
print(f"  config_1: {config_1}")
print(f"  config_2: {config_2_independent}\n")

assert config_1 is not config_2_independent
assert config_1["participants"] is not config_2_independent["participants"]
assert config_1["launch_params"] is not config_2_independent["launch_params"]
assert config_1 == {
    "name": "Task Tracker v1.0",
    "participants": ["Иванов", "Петров"],
    "launch_params": {
        "host": "localhost",
        "port": 8080,
        "debug": False
    },
}
