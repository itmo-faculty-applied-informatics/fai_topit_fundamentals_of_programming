import math

x = 17
y = 5
print(x+y, type(x+y))
print(x-y, type(x-y))
print(x*y, type(x*y))
print(x/y, type(x/y))
print(x//y, type(x//y))
print(x%y, type(x%y))
print(x**y, type(x**y))

print('------------------------------------')

print(2**1000, type(2**1000), sep = '\n')

print('------------------------------------')

result = 0.1 + 0.2
print(result)
print(result == 0.3)
print(result - 0.3)
print(math.isclose(result, 0.3))

print('------------------------------------')

print(int("42"), type(int("42")))
print(float("3.14"), type(float("3.14")))
print(str(2026), type(str(2026)))
print(bool(0), type(bool(0)))
print(bool(-1), type(bool(-1)))
print(bool(""), type(bool("")))
print(bool('False'), type(bool("False")))
print(complex(2, -3), type(complex(2, -3)))
print("Действительная часть:", complex(2, -3).real)
print("Мнимая часть:", complex(2, -3).imag)
