__author__ = 'Agafonova Anna'

# Задача-4: Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = input("Enter number: ")
x = 0
for i in number:
    while int(i) > x:
        x = int(i)
print(x)

