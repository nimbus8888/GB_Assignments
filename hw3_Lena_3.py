# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.

def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 >= arg2 and arg1 <= arg3:
        return arg1 + arg3
    else:
        return (arg2 + arg3)

# my_func(arg1 = int(input('Введите 1 - ')), arg2 = int(input('Введите 2 - ')), arg3 = int(input('Введите 3 - ')))
result = my_func(arg1 = int(input('Введите 1 - ')), arg2 = int(input('Введите 2 - ')), arg3 = int(input('Введите 3 - ')))
print(result)




