# Очень простой калькулятор

# Ввод чисел
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Выбор операции
print("Выберите операцию:")
print("1 - Сложение")
print("2 - Вычитание")
print("3 - Умножение")
print("4 - Деление")

operation = input("Введите номер операции: ")

# Выполнение операции
if operation == "1":
    print("Результат:", num1 + num2)
elif operation == "2":
    print("Результат:", num1 - num2)
elif operation == "3":
    print("Результат:", num1 * num2)
elif operation == "4":
    if num2 != 0:
        print("Результат:", num1 / num2)
    else:
        print("Ошибка: деление на ноль!")
else:
    print("Неверный ввод!")
