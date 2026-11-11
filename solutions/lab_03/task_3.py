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

def add_record(student, lab, score):
    submissions.append((student, lab, score))
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

add_record("Ivan", "lab_01", 5)

print(submissions)
print(set_students)
print(set_labs)
print(dictionary_attempts)
print(dictionary_best)
print(attempts_count)

set_both = set_lab1 & set_lab2
print(set_both)


# Практическое расширение

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