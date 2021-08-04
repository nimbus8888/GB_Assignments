# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

month = int(input('Введите порядковое число месяца - '))
if 9 < month <= 12 or 1 <= month <= 3:
    print('Зима')
elif 4 <= month <= 5:
    print('Весна')
elif 6 <= month <= 8:
    print('Осень')
elif month == 9:
    print('Осень')
else:
    print('Что-то пошло не так')

# months_dict = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May',
#              '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October',
#              '#11': 'November', '12': 'December'}