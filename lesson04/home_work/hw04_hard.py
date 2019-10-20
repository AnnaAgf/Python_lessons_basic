import my_module
import random
from itertools import permutations



'''print(random.randint(0, 10))
print(random.randrange(5))
print(random.randrange(0, 100, 5))
print(random.random() + 1)

print(my_module.my_func(2, 5))
my_module.my_msg()

my_list = [1, 2, 3, 4, 5]
new =[el * 10 for el in my_list if el % 2 == 1]
new2 = {el: el * 3 for el in my_list if el % 2 == 1}
print(new2)
print(random.choices(my_list))'''

''''''def generator():
    for el in (10, 20, 30):
        yield el
g = generator()
print(g)
for el in g:
    print(el)