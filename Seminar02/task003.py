# 3.	Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

str_sub = input('Введите подстроку: ')
str_src = input('Введите строку, в которой подсчитывать количество вхождений подстроки: ')
#sa = 'abc'
#sb = 'dsfdfgabcsafsabcsadfabc'

def count_substings(source, subsr):
	len_substr = len(subsr)
	len_source = len(source)
	i = 0
	for iend in range(len_substr, len_source+1):
		#print(source[iend-len_substr:iend])
		if source[iend-len_substr : iend] == subsr:
			i+=1
	return i

print(f'Число вхождений строки "{str_sub}" в строку "{str_src}" = ', count_substings(str_src, str_sub))
print(f'Проверка с помощью str.count() -> {str_src.count(str_sub)}')
