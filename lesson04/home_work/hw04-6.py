'''Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.'''
from itertools import count
from itertools import cycle

def my_count_func(start_number, stop_number):
    for el in count(start_number):
        if el > stop_number:
            break
        else:
            print(el)
def my_cycle_func(start_number, stop_number):
    for el in cycle(start_number):
        if el > stop_number:
            break
        else:
            print(el)
my_count_func(start_number = int(input("enter start number: ")), stop_number = int(input("enter stop number: ")))
my_cycle_func(start_number = int(input("enter start number: ")), stop_number = int(input("enter stop number: ")))