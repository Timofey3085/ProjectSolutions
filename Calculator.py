"""
Написал простой калькулятор и с помощью сборщика PyInstaller
упаковал код для возможности запуска без использования IDE.
Пример команды: pyinstaller --onefile calculator.py
"""


def calculate(x: int, y: int, operator: str) -> float:
    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "/":
        return x / y
    elif operator == "*":
        return x * y
    elif operator == "**":
        return x ** y
    else:
        print("Некорректный оператор. Введите арифметическое действие (+, -, /, *, **): ")
        new_operator: str = input()
        return calculate(x, y, new_operator)


operator: str = input("Введите арифметическое действие (+, -, /, *, **): ")
x = int(input("Введите первое число: x = "))
y = int(input("Введите второе число: y = "))

result = calculate(x, y, operator)
print("Результат:", round(result))

input("Press Enter to exit...")