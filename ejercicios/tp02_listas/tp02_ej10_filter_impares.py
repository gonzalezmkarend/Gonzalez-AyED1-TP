
from random import randint

lista = [randint(1, 100) for num in range(30)]
print(lista)

filtrada = list(filter(lambda num: num % 2 != 0, lista))
print(filtrada)