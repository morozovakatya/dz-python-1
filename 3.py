# Напишите программу, которая по заданному 
# номеру четверти, показывает диапазон возможных 
# координат точек в этой четверти (x и y).

def inputNum(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = int(input(f"Введите координату по {xy[i]}: "))
                a.append(number)
                is_OK = True
            except ValueError:
                print("Ты ошибся. Вводить надо целые числа!")
    return a


def lengthSegment(a, b):
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return lengthSegment


print("Введите координаты точки А")
pointA = inputNum(2)
print("Введите координаты точки В")
pointB = inputNum(2)

print(f"Длина отрезка: {format(lengthSegment(pointA, pointB), '.2f')}")