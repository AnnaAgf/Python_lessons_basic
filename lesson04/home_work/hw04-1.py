# Задание-1:
'''Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.'''

from sys import argv

file_name, worked_hour, rate, benefit = argv

calculation = (int(worked_hour) * int(rate)) + int(benefit)
print(f"Your pay is equal {calculation}")