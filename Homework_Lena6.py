# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3

km = float(input('Сколько км пробежал в первый день? '))
b = float(input('Цель в км'))
i = 1
while km < b:
    km *= 1.1
    i += 1
print(i)

