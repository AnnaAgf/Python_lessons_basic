__author__ = 'Agafonova Anna'

# Задача-3: Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = input("Enter number: ")
a = int(number + number)
b = int(number+number+number)
summa = int(number) + a + b

print(summa)