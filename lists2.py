rabbits = ['Пушок', 'Дружок', 'Мурзик', 'Барсик', 'Эдуард', 'Ушастик', 'Роджер', 'Трус']
rabbits[0:7:2]
rabbits[:7:2]
rabbits[0::2]
rabbits[::2]
rabbits[7::-2]
rabbits[:0:-2]
rabbits[::-2]

sparta = ['Иванов', 'Петров', 'Сидоров', 'Зайцев', 'Дятлов', 
          'Козлов', 'Лисичкин', 'Огурцов', 'Капустин', 'Арбузов']
sparta[::2]
sparta[0:9:5]
sparta[::-3]
sparta[-2:1:-3]

my_list = [1, 2, 3, 4, 5]
my_list.append(100500)
print(my_list)

old_salary = [35000, 50000, 65000, 49000, 55000]
new_salary = []
for salary in old_salary:
    new_salary.append(salary * 1.9)
print(new_salary)


my_list = [10, 65, 31, 29, 90, 87, 100]
my_list.sort(reverse = False)
print(my_list)

my_list = ['банан', 'дыня', 'апельсин', 'груша', 'вишня']
my_list.sort(reverse = True)
print(my_list)


salary = [100000, 45000, 78000, 29000, 55000, 60000, 55000]
print(min(salary)) 
print(max(salary)) 
print(salary.count(55000))


names = ['Андрей', 'Илья', 'Александр', 'Ипполит', 'Анна', 'Константин', 'Елена', 'Мария']
my_list = []
for name in names:
    my_list.append(len(name))
name_length = min(my_list)
result = my_list.count(name_length)
print(result)

my_list = [1, 10, 45, 31, 12, 54, 111, 398, 97, 63]
my_list.sort(reverse = True)
print(my_list[2])
      


my_list = [1]
for i in range(10):
    my_list.append(my_list[i] * 2)
my_list.sort(reverse = True)
print(my_list)
print(min(my_list))
print(max(my_list))
my_list[5]



fruits = 'яблоко банан апельсин баклажан перец помидор арбуз ананас'.split()
my_list = []
for fruit in fruits:
    my_list.append(fruit[0])
my_list.sort()
print(fruits)
print(my_list)


#Напишите программу, которая создаёт список, содержащий целые, кратные трём числа в интервале от 1 до 50. 
#Найдите сумму элементов этого списка. Результат вычислений сохраните в переменной с именем result.
a_list = []
for n in range(1,51):
    if n % 3 == 0:
        #print(n)
        a_list.append(n)
#print(a_list)
result=sum(a_list)
print(result)



#Напишите программу, которая создаёт список my_list, содержащий длины слов из списка raw_list (дан в начале кода), 
#и находит сумму минимального и максимального элементов нового списка (my_list). 
#Результат вычислений (сумма минимального и максимального элементов списка my_list) присвойте переменной result.

raw_list = ['переменные', 'циклы', 'условия', 'списки', 'словари', 'файлы', 'функции']
my_list = []
for e in raw_list:
    print(len(e))
    my_list.append(len(e))
    #print(my_list)               
print(my_list)
print(min(my_list))
print(max(my_list))                   
result=min(my_list) + max(my_list)
print(result)                   


#Дан список raw_list (содержимое списка приведено в начале кода). 
#Найдите минимальное (x_min) и максимальное (x_max) значения элементов данного списка.
#Создайте новый список my_list, состоящий из элементов списка raw_list, умноженных на x_min, 
#если элемент является чётным числом, и на x_max, в случае если элемент нечётный.

#Найдите максимальное значение списка my_list. Результат присвойте переменной result.

raw_list = [2, 8, 10, 23, 64, 49, 11, 52, 71, 14]
x_min = min(raw_list)
x_max = max(raw_list)
my_list = []
for i in raw_list:
    if i % 2 == 0: 
        my_list.append(i * x_min)
    else:
        my_list.append(i * x_max)
result = max(my_list)
print(result)

#Дана статистика результатов рекламной кампании по каналу (ключ 'source') и сумме расходов ('cost').
#Напишите код, который ищет минимальное значение ключа cost в этом словаре. 

results = [
    {'cost': 98, 'source': 'vk'},
    {'cost': 153, 'source': 'yandex'},
    {'cost': 110, 'source': 'facebook'},
]
my_list = []
for r in results:
    my_list.append(r['cost'])
print( min(my_list))

#-------------------------------------------
L = ['a', 'b', 'c']
print(id(L))

L.append('d')
print(id(L))
#-------------------------------------------

#Используя цикл while, найдите первое целое число, которое не кэшируется в памяти.
a = 0
b = 0

while id(a) == id(b):
    a += 1
    b += 1

print(a)
#257

#--------------------------
# Если мы сохраняем в две переменные одинаковые малые числа, то эти переменные будут равны в двух смыслах: 
#их значения равны (проверяем через ==), и 
#они ссылаются на одинаковые объекты (проверяем через is).

a = 42
b = 42

print(a == b)
# True

print(a is b)
# True

#Однако, если мы проделаем то же самое, но с числами, превышающими границу, найденную в задании, то результат окажется несколько иным.

c = 123456789
d = 123456789

print(c == d)
# True

print(c is d)
# False
#------------------------------

L = ['Hello', 'world']
M = L

print(M is L)
# True

M.append('!')

print(L)
# ['Hello', 'world', '!']
#Чтобы избежать такого поворота событий, список нужно копировать:
M = L.copy()

print(M is L)
# False
#--------------------

shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])

shopping_center[-1].append("Uniqlo")

print(shopping_center)
# ('Галерея', 'Санкт-Петербург', 'Лиговский пр., 30', ['H&M', 'Zara', 'Uniqlo'])


