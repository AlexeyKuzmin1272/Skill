def linear_solve(a, b):
    return b / a

# 2*x = 9
print(linear_solve(2, 9))
#------------------------------------
def linear_solve(a, b):
    if a: # помним, что 0 интерпретируется как False, иначе True
        return b / a
    else:
        return "Нет корней"

print(linear_solve(0,1))
#------------------------------------
def linear_solve(a, b):
    if a: 
        return b / a
    elif not a and not b: # снова используем числа в логических выражениях
        return "Бесконечное количество корней"
    else:
        return "Нет корней"
print(linear_solve(0,0))
#------------------------------------
#Реализуйте функцию quadratic_solve(a, b, c), возвращающую «Нет вещественных корней» в случае отрицательного дискриминанта.
def quadratic_solve(a, b, c):
    if D (a, b) < 0:
        print ('Нет вещественных корней')
#------------------------------------
#Реализуйте функцию quadratic_solve(a, b, c), возвращающую «Нет вещественных корней» в случае отрицательного дискриминанта.
#модифицируем функцию таким образом, чтобы при нулевом дискриминанте возвращалось значение единственного корня.
def quadratic_solve(a, b, c):
    di = D (a, b, c)
    if di < 0:
        return "Нет вещественных корней"
    elif di == 0:
        return -b/(2*a)
    else:
        return (-b - D(a,b,c) ** 0.5) / (2 * a), (-b + D(a, b, c) ** 0.5) / (2 * a)

print(quadratic_solve(1, 0, -1))

#------------------------------------
L = list(map(int, input().split(' ')))
L
print(quadratic_solve(*L))
#------------------------------------
Представим, что аргументы теперь хранятся не в виде списка, а в виде словаря.

M = {'a': 1,
     'b': 0,
     'c': -1}
M.values()
print(quadratic_solve(**M))
#Оператор распаковки словаря (**) 
#------------------------------------
#Напишите рекурсивную функцию, находящую минимальный элемент списка без использование циклов и встроенной функции min().
def min_list(iL):
    if len(iL) == 1:
        return iL[0]
    
    if iL[0] < min_list(iL[1:]):
        return iL[0]
    else:
        return min_list(iL[1:])
    
L = [3,4,2,5,8,-7]
print(min_list(L))

#------------------------------------
#Напишите рекурсивную функцию, которая зеркально разворачивает число. Предполагается, что число не содержит нули.

def mirror(a, res=0):
    return mirror(a // 10, res*10 + a % 10) if a else res 

print(mirror(5678))

def revers2char(digs):
    lst = str(digs)
    chars = list(lst)
    res_s = ''
    #print(chars)
    #new_proverb = ''
    for d in lst:
        res_s = d + res_s
    return(int(res_s))


#------------------------------------
##реализовать функцию equal(N, S), проверяющую, совпадает ли сумма цифр числа N с числом S. 
#При написании программы следует обратить внимание на то, что, если S стала отрицательной, 
#то необходимо сразу вернуть False.
def sum_digits (N):
    if N == 0:
        return 0
    return N % 10 + sum_digits(N // 10)
#print(341 // 10)
#print(341 % 10)
print(sum_digits(341))

def equal(N, S):
    #print(str(N) + ' ' + str(S))
    #print(N == S)
    if S < 0:
        return False
    
    if N == S:
        return True
    else:
        return equal(N // 10, S - (N % 10))
   
print(equal(100,1)) 
#------------------------------------
def e():
    n = 1
    
    while True:
        yield (1 + 1 / n) ** n
        n += 1
    
last = 0
cnt = 0
for a in e(): # e() — генератор
    cnt +=1
    if (a - last) < 0.00000000000001: # ограничение на точность
        print(a)
        print(cnt)
        break # после достижения которого — завершаем цикл
    else:
        last = a # иначе — присваиваем новое значение     
#print(last)    
#------------------------------------
USERS = ['admin', 'guest', 'director', 'root', 'superstar']

yesno = input("""Введите Y, если хотите авторизоваться, или N, 
             если хотите продолжить работу как анонимный пользователь: """)

auth = yesno == "Y"

if auth:
    username = input("Введите ваш username:")

def is_auth(func):
    def wrapper():
        if auth:
            print("Пользователь авторизован")
            func()
        else:
            print("Пользователь неавторизован. Функция выполнена не будет")
    return wrapper

def has_access(func):
    def wrapper():
        if username in set(USERS): #== 'admin' :
            print("Пользователь имеет доступ")
            func()
        else:
            print("Пользователь не имеет доступа. Функция выполнена не будет")
    return wrapper

@is_auth
@has_access
def from_db():
    print("some data from database")

from_db()
#------------------------------------
#------------------------------------
#------------------------------------
