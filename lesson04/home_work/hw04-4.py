'''Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.'''
from itertools import permutations
from itertools import repeat
from itertools import combinations
'''for el in repeat('j', 6):
        print(el)'''
for el in combinations('j', 6):
    if el > 3:
        break
    else:
        print(el)
