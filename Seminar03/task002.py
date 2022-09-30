# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

def find_pos(lst, string):
    string = str(string)
    i = 0
    count = 0
    while i < len(lst):
        if lst[i] == string:
            count += 1

        if count == 2:
            return i

        i += 1

    return None

sources = [["qwe", "asd", "zxc", "qwe", "ertqwe"],
["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"],
["йцу", "фыв", "ячс", "цук", "йцукен"],
["123", "234", 123, "567"],
[]]

search_patterns = ['qwe','йцу','йцу','123','123']

positions = [find_pos(sources[i], search_patterns[i]) for i in range(len(sources))]

for i in range(len(positions)):
	print(sources[i], f'ищем "{search_patterns[i]}"', ' -> ', positions[i])

# source_lst1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# source_lst2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# source_lst3 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
# source_lst4 = ["123", "234", 123, "567"]
# source_lst5 = []

# search1 = 'qwe'
# search2 = 'йцу'
# search3 = 'йцу'
# search4 = '123'
# search5 = '123'

# pos1 = find_pos(source_lst1, search1)
# pos2 = find_pos(source_lst2, search2)
# pos3 = find_pos(source_lst3, search3)
# pos4 = find_pos(source_lst4, search4)
# pos5 = find_pos(source_lst5, search5)

# print(source_lst1, f'ищем "{search1}"', ' -> ', pos1)
# print(source_lst2, f'ищем "{search2}"', ' -> ', pos2)
# print(source_lst3, f'ищем "{search3}"', ' -> ', pos3)
# print(source_lst4, f'ищем "{search4}"', ' -> ', pos4)
# print(source_lst5, f'ищем "{search5}"', ' -> ', pos5)
