# Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
answer = []

for i in range(len(my_list)-1):
    if my_list[i] < my_list[i+1]:
        answer.append(my_list[i+1])

print(answer)
