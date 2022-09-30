# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

lst_str = ['sdgfdf46ss57ddfsd',
           'dsfs44df84hgy',
           '13rtddcvgfh',
           'ge123rgfvxc',
           'dgd5674fgfgh']


def find_index(lst, number):
    number_str = str(number)
    i = 0
    while i < len(lst):
        if (lst[i].find(number_str) != -1):
            return i
        i += 1
    return -1


num = int(input('Введите искомое число: '))

idx = find_index(lst_str, num)
if idx >= 0:
    print(
        f'Искомое число {num} найдено в строке "{lst_str[idx]}" (номер строки в списке {idx+1})')
else:
    print(f'Искомого числа {num} нет в исходном списке')

# вариант: выводим номера позиций строк где найдено число
res = [idx+1 if item.find(str(num)) > 0 else -
       1 for (idx, item) in enumerate(lst_str)]
res = list(filter(lambda item: item != -1, res))
print('Список позиций строк в списке, содержащих искомое число: ', res)
