# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!

from math import factorial

def fact_gen(number):
    fact_num = 1
    if number == 0:
        yield f'{number}! = 1'
    for i in range(1, number + 1):
        fact_num *= i
        yield f'{i}! = {fact_num}'

for el in fact_gen(int(input('Factorial number: '))):
    print(el)

