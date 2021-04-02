L = [1,1,2,3,2]

b = set(L)

print(b)
# {1,2,3}
b_list = list(b)

print(b_list)
# [1,2,3]

# одной строкой выюираем уникальные элементы в список
c = list(set(L))

print(c)
# [1,2,3]

#Напишите программу, которая на вход принимает текст и выводит количество уникальных символов.
i_text = 'Некий исходный произвольный текст'
print (set(i_text)) 
o_text = list(set(i_text))

# найдите количество уникальных символов в тексте.
i_text = ('The Zen of Python \n '+\
          'Beautiful is better than ugly. \n'+\
          'Explicit is better than implicit.\n'+\
          'Simple is better than complex.\n'+\
          'Complex is better than complicated.\n'+\
          'Flat is better than nested.\n'+\
          'Sparse is better than dense.\n'+\
          'Readability counts.\n'+\
          'Special cases aren\'t special enough to break the rules.\n'+\
          'Although practicality beats purity.\n'+\
          'Errors should never pass silently.\n'+\
          'Unless explicitly silenced.\n'+\
          'In the face of ambiguity, refuse the temptation to guess.\n'+\
          'There should be one-- and preferably only one --obvious way to do it.\n'+\
          'Although that way may not be obvious at first unless you\'re Dutch.\n'+\
          'Now is better than never.\n'+\
          'Although never is often better than *right* now.\n'+\
          'If the implementation is hard to explain, it\'s a bad idea.\n'+\
          'If the implementation is easy to explain, it may be a good idea.\n'+\
          'Namespaces are one honking great idea -- let\'s do more of those!'
)
#print (set(i_text)) 
l_set = set(i_text)
print(len(l_set) - 1)
#----------------------------------------------
#set.union(other)	Объединение	Возвращает множество, состоящее из элементов set и other.
#set.intersection(other)	Пересечение	Возвращает множество, состоящее из элементов, которые встречаются и в set, и в other.
#set.difference(other)	Разность	Возвращает множество элементов set, которые не встречаются в other.
#set.symmetric_difference(other)	Симметричная разность	Возвращает множество элементов, встречающихся в одном из множеств, но не в обоих одновременно.
#----------------------------------------------

# Представленная ниже программа должна находить множество символов, которые встречаются в двух строках одновременно.
a = input("Введите первую строку: ")
b = input("Введите вторую строку: ")

a_set, b_set = set(a), set(b) # используем множественное присваивание

a_and_b = a_set.intersection(b_set)

print(a_and_b)
#-----------------------------------------------

#Напишите программу, которая на вход получает две последовательности целых чисел, а возвращает список элементов, 
#встречающихся только в одной из последовательностей. Какую операцию над множествами вы использовали? 
#Введите только название метода без скобок.

#symmetric_difference
 
#Напишите числа в порядке возрастания через пробел, которые выведет программа из предыдущего задания, 
#если на вход подаются две последовательности чисел:

1 2 3 4 5 6 7 8
2 4 6 8 10 12

1 3 5 7 10 12


