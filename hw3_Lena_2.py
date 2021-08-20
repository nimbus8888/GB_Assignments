# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user(name, last_name, year, town, email, phone):
    print(f"name - {name}; last_name - {last_name}; year - {year}; town - {town}, email - {email}; phone - {phone}")

print (user(name = input('Введите name - '), last_name = input('Введите surname - '), year = input('Введите birthday - '), town = input('Введите city - '), email = input('Введите email - '), phone = input('Введите phone - ')))

