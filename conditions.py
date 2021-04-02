flower = 'роза'
color = 'фиолетовый'
if flower == 'роза':
    if color == 'синий' or color == 'белый':
        print ("Ане понравятся эти цветы")
    else:
        print ("Аня не любит такие цветы")
else:
    print ("Аня не любит такие цветы")

height = 180
weight = 92
color = 'синий'
if height > 170 and weight < 80 and color == 'красный':
    print ("Ваша половинка нашлась!")
else:
    print ("Попробуем поискать ещё...")


number = 346
if number % 2 == 0 or number % 5 == 0 or number % 173 == 0 or number % 821 == 0:
    print("Вова, это нужное число")
else:
    print("Вова, в этот раз ты не попал")


fav_word = 'Аппликация'
if fav_word in ["рептилия", "питон", "змея"]:
    print("Python")
elif fav_word in ["плюс", "плюсы"]:
    print("C++")
elif fav_word in ["рубин","кристалл"]:
    print("Ruby")
else:
    print("Python")



hour = 18 
minute = 47
dayminutes = hour * 60 + minute
if dayminutes <= 10*60 or dayminutes >= 20*60:
    print("Преподаватель - дома")
elif (dayminutes >= 10*60+30 and dayminutes <= 12*60) or (dayminutes >= 13*60+40 and dayminutes <= 15*60) or (dayminutes >= 18*60 and dayminutes <= 19*60+30):
    print("Преподаватель занят.")
else:     
    print("Преподаватель свободен.")

#------------------------
if some_var is None:
    print("NoneType")
else:
    print(type(some_var))

#------------------------
a = None # пустая строка
b = a or 1
#b = a if a is not None else 1
print (b)

#------------------------
a = "foo"
b = "bar"

print(1 and a or b)

#------------------------

a = ""
b = "bar"

print(1 and a or b)

#------------------------

# пусть a и b - переменные, которые мы хотим проверить
if a and b : # проверка истинности обеих переменных
    print("Обе переменные истинные")
    print(a,b)
#--------------------------

# пусть a и b - переменные, которые мы хотим проверить
if a and b:
    print("Обе переменные истинные")
    print(a,b)
elif a or b:
    print("Одна из переменных истинная")
    print( a or b ) # печать значения одной переменной, которая является истинной
#----------------------------------------

#  мы хотим проверить, является ли оно целым, 
# находится ли в определённом промежутке (например, от 100 до 999 включительно), 
#да ещё и делится ли на 2 и 3 одновременно. 
import locale

locale._override_localeconv["thousands_sep"] = ""
locale._override_localeconv["decimal_point"] = "."

#locale.atof('123456,78')

a = locale.atof(input('Введите число '))
print(a)
if a == int(a) and a >= 100 and a <= 999 and a % 2 == 0 and a % 3 == 0:
    print ('Условие выполнилось')
else:
    print ('Условие не выполнилось')
#----------------------------------------
#некорректное решение
import locale

locale._override_localeconv["thousands_sep"] = ""
locale._override_localeconv["decimal_point"] = "."

#locale.atof('123456,78')

a = locale.atof(input('Введите число '))
print(type(a))
if all([type(a) == int,
       100 <= a <= 999,
       a % 2 == 0,
       a % 3 == 0]):
    print ('Условие выполнилось')
else:
    print ('Условие не выполнилось')

#--------------------------
#Напишите программу, которая на вход принимает последовательность целых чисел и возвращает True, если все числа ненулевые, 
#и False, если хотя бы одно число равно 0.
L = list(map(int, input().split(',')))

print(all(L))

#------------------------------
#Напишите программу, которая на вход принимает последовательность целых чисел и возвращает True, если все числа равны нулю, 
#и False, если найдётся хотя бы одно ненулевое число. Разрешается использование только логических операторов и функций all([ ]) и any([ ]).
L = list(map(int, input().split(' ')))
print(any(L))
#------------------------------
