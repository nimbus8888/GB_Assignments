# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк

time = int(input('cек'))
sec = time % 60
h = time // 3600
min_ = time // 60 - h*60
if time >= 86401:
    print('Больше суток')
else:
    print(f'{h:02}: {min_:02} : {sec:02}')
