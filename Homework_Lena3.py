# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.
n = input('Put the number here, please')
nn = {n + n}
nnn = {n + n + n}
all_together = int(n) + int(n + n) + int(n + n + n)
print(all_together)
