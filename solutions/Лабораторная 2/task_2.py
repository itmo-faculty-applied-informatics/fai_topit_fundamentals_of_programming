import copy

original = [
    ["Python", 5],
    ["Algorithms", 4],
]

alias = original
shallow = original.copy()
deep = copy.deepcopy(original)

original.append(["Databases", 5])
print('Значения:')
print(f'original: {original}\nalias: {alias}\nshallow: {shallow}\ndeep: {deep}\n')
print('Идентификаторы внешних списков:')
print(f'original: {id(original)}\nalias: {id(alias)}\nshallow: {id(shallow)}\ndeep: {id(deep)}\n')
print('Идентификаторы первого вложенного списка в каждой структуре:')
print(f'original: {id(original[0])}\nalias: {id(alias[0])}\nshallow: {id(shallow[0])}\ndeep: {id(deep[0])}\n')
print('Идентификаторы объекта, содержащего первую оценку:')
print(f'original: {id(original[0][1])}\nalias: {id(alias[0][1])}\nshallow: {id(shallow[0][1])}\ndeep: {id(deep[0][1])}\n')

print('-----------------------------------------------')
original[0][1] = 3
print('Значения:')
print(f'original: {original}\nalias: {alias}\nshallow: {shallow}\ndeep: {deep}\n')
print('Идентификаторы внешних списков:')
print(f'original: {id(original)}\nalias: {id(alias)}\nshallow: {id(shallow)}\ndeep: {id(deep)}\n')
print('Идентификаторы первого вложенного списка в каждой структуре:')
print(f'original: {id(original[0])}\nalias: {id(alias[0])}\nshallow: {id(shallow[0])}\ndeep: {id(deep[0])}\n')
print('Идентификаторы объекта, содержащего первую оценку:')
print(f'original: {id(original[0][1])}\nalias: {id(alias[0][1])}\nshallow: {id(shallow[0][1])}\ndeep: {id(deep[0][1])}\n')

print('-----------------------------------------------')

wrong_matrix = [[0] * 3] * 3
wrong_matrix[0][0] = 1
print('wrong_matrix:', wrong_matrix)

correct_matrix = [[0] * 3 for _ in range(3)]
correct_matrix[0][0] = 1
print('correct_matrix:', correct_matrix)