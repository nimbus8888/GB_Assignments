#Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль

def two(arg_1, arg_2):


    try:
        arg_1 = int(arg_1)
        arg_2 = int(arg_2)
        two_numbers = arg_1 / arg_2
    except ValueError:
        return 'Ошибка'
    except ZeroDivisionError:
        return 'Деление на 0!'
    return round(two_numbers, 2)

print(two(input('Введите первое число - '), input('Введите второе число - ')))


