# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


def salary():
    try:
        production_per_hour, rate_per_hour, bonus = map(float, argv[1:])
        print(f'Salary = {production_per_hour * rate_per_hour + bonus}')
    except ValueError:
        print('Hmmm')


salary()




