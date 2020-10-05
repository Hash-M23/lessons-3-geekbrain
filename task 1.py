def main(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Ошибка деления"


x = int(input("Введите число для деления"))
y = int(input("Введите число"))

print(main(x, y))