squares = [i**2 for i in range(1,11)]
print(squares)
squares1 = [i**2 for i in range(1,11) if i % 2 == 1]
print(squares1)
#----------------------------------------------
#��� ������ ���������� ������� �������� ������� ��������� ����� �� 1 �� 10
m_table = [[i*j for j in range(1,11)] for i in range(1,11)]
print(m_table)
#----------------------------------------------
L = [input() for i in range(5)]

L = [int(input()) for i in range(5)]
print(L)
#---------------------------------------------- \
import locale
x = '12'
print(locale.localeconv().get('decimal_point'))
print(locale.atoi(x))
print(locale.atof(x))
#----------------------------------------------
squares = [i**2 for i in range(1,11)]
print(squares)
squares1 = [i**2 for i in range(1,11) if i % 2 == 1]
print(squares1)

#----------------------------------------------
#��� ������ ���������� ������� �������� ������� ��������� ����� �� 1 �� 10
max_n = 8
m_table = [[i*j for j in range(1,max_n + 1)] for i in range(1,max_n + 1)]
#print(m_table)
# ������������ ������ ������� float
for j in range(1,11): #max_n + 1):
    for i in range(1,max_n + 1):
        s = '{:2} x {:2} = {:2}'.format(j,i, i*j)
        print(s, end = '   ')
    print('', end = '\n')    
        
#num = "{:{align}{width}.{precision}f}"

# �������� ����� ������� � �������� ����������
#print("{:{align}{width}.{precision}f}".format(123.236, align='<', width=8, precision=2))

#print("{:2d}".format(m_table[0]))
#for n in enumerate(m_table, 1):
#    print ("{:2d}".format(n))
#print('----------------------------')
#print(fill(str(m_table), width=10) )

#----------------------------------------------
print('{:2}:{:2}'.format(1, 2))
#----------------------------------------------
M = [[i+j for j in range(5)] for i in range(5)]
print(M)
#----------------------------------------------
T = [[i*j for j in range(1,11)] for i in range(1,11)]
print(T)
#----------------------------------------------
#print(33 % 2 == 1)
T = [[i * j % 2 == 1 for j in range(1,11)] for i in range(1,11)]
print(T)
#----------------------------------------------
L = [int(input()) for i in range(5)]
print(L)
#----------------------------------------------
#������������� ��������� ������ ����� �������, ����� � ������ ����������� 
#True, ���� ������� ������, � False, ���� ������� ��������.
L = [int(input()) % 2 == 0 for i in range(2)]
print(L)
#----------------------------------------------
#�������� ����� �?� ����� �������, ����� ��������� �������� True, ���� ���� ���� �� ���� ������ �����.
L = [int(input()) % 2 == 0 for i in range(2)]
print( any(L))
#----------------------------------------------
# ��� ��������� ����� �������� ����� � ������ �����, 
# ����� � ������ ���� ���� �� ���� ������ � ���� �� ���� �������� �������.
L = [int(input()) % 2 == 0 for i in range(2)]
print(any(L) and not all(L))
#----------------------------------------------
L = [i for i in range(10)]
# 0 1 2 3 4 5 6 7 8 9
M = [i for i in range(10,0,-1)]
# 10 9 8 7 6 5 4 3 2 1
for a, b in zip(L,M):
    print('a =', a, ',  b =', b)
#----------------------------------------------
#��������� ������� zip() ������ ����������� �������, ��������� ������������ ������������ ������� L � M.
L = [i for i in range(10)]
M = [i for i in range(10,0,-1)]

for a, b in zip(L,M):
    print('a x b =', a*b)

N = [a*b for a,b in zip(L,M)]
print(N)
#----------------------------------------------
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]    # ����� � ��� ���� �������� ������
list_b = [x for x in list_a]           # �������� ����� ������ ��������� ��������� ������
print(list_b)                          # [-2, -1, 0, 1, 2, 3, 4, 5]
print(list_a is list_b)                # False - ��� ������ �������!

#----------------------------------------------
 # if x % 2 == 0 - ������� �� ������� �� 2 ����� ���� - ����� ������
list_a = [-2, -1, 0, 1, 2, 3, 4, 5] 
list_b = [x for x in list_a if x % 2 == 0]
print(list_b)   # [-2, 0, 2, 4]
#----------------------------------------------
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
list_b = [x for x in list_a if x % 2 == 0 and x > 0]
# ����� �� x, ������� ������������ ������ � ������ ����
print(list_b)   # [2, 4]
#----------------------------------------------
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
list_b = [x**2 for x in list_a]
print(list_b)   # [4, 1, 0, 1, 4, 9, 16, 25]

#----------------------------------------------
list_a = ['a', 'abc', 'abcde']
list_b = [len(x) for x in list_a]
print(list_b)   # [1, 3, 5]
#----------------------------------------------
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
list_b = [x if x < 0 else x**2 for x in list_a]
# ���� x-������������� - ����� x, � ��������� ������� - ����� ������� x
print(list_b)   # [-2, -1, 0, 1, 4, 9, 16, 25]
#----------------------------------------------
#����� �� ��������� ������������� ���������� � ���������:

list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
list_b = [x**3 if x < 0 else x**2 for x in list_a if x % 2 == 0]
# ������� ������ ���������� � ��������� ������ ������ ��������
# ����� ����� ��������� � ��������� ��� ������������� �������� � ���, � ��� ��������� � �������
print(list_b)   # [-8, 0, 4, 16]
#----------------------------------------------
numbers = range(10)

# Before
squared_evens = [n ** 2 for n in numbers if n % 2 == 0]

# After
squared_evens = [
    n ** 2
    for n in numbers
    if n % 2 == 0
]
squared_evens
#----------------------------------------------
#��� ������� ������� ������� ������ � ������� �� ������ ����� ������ ��������� ������ ����� � ����� ��
#� ������� ���� ������ ��������:

#3.1 ������� � ������� ���������� ������

numbers = range(10)
squared_evens = [n ** 2 for n in numbers if n % 2 == 0]
print(squared_evens)   # [0, 4, 16, 36, 64]

#3.2. ������� c ������� ����� for
#�����: ������ ��������� ��������� ����� ���������� � ���� ����� for, �� �� ������ ���� for ����� ����������� �
#���� ������ ���������.

numbers = range(10)
squared_evens = []
for n in numbers:
    if n % 2 == 0:
        squared_evens.append(n ** 2)
print(squared_evens)   # [0, 4, 16, 36, 64]

#� �����, ��� ����� ������� � ����������� �����, ������� � ���� ����� ����� ���� �������� � ����� 
#��������� � ���������. ��� ����� ������� �����, ��������� ���������-���������� ����� ���������� � ����� � ������.

#3.3. ������� � ������� �������.

#��� ������, ������, ��� ��������� ���������� � ���������� ��������� � ��� ���� �������������� �����, 
#�� ����� ����� � ����������������.
#����� ��������� � ����� ������ �������������� ������� ��� ������� ��� �� �����, ���������� map(), lambda � filter().

numbers = range(10)
squared_evens = map(lambda n: n ** 2, filter(lambda n: n % 2 == 0, numbers))
print(squared_evens)         # <map object at 0x7f661e5dba20>
print(list(squared_evens))   # [0, 4, 16, 36, 64]
# ����������: � Python 2 � ���������� squared_evens �������� ����� ������, 
#� � Python 3 �map object�, ������� �� ���������� � ������ � ������� list()

#�������� �� ��, ��� �������� ������ ������ �������, �������� �� ������ � ������������� ���������� ����������� 
#��������� ����� ����� ��������������� � ��������.

#----------------------------------------------
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
my_gen = (i for i in list_a)    # ���������-���������
print(next(my_gen))     # -2 - �������� ��������� ������� ����������
print(next(my_gen))     # -1 - �������� ��������� ������� ����������
#----------------------------------------------
#����������� ���������-�����������

#��������� ������ ������ ��� ������ � ��� �������������� ������.
# my_gen = i for i in list_a      # SyntaxError: invalid syntax

#��� �������� � ������� �������������� ������ �������������
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
my_sum = sum(i for i in list_a)
# my_sum = sum((i for i in list_a))  # ��� ���� �����
print(my_sum)   # 12

#������ �������� ����� �������� len()
# my_len = len(i for i in list_a)  # TypeError: object of type 'generator' has no len()

#������ ����������� �������� �������� print()
print(my_gen)   # <generator object <genexpr> at 0x7f162db32af0>

#�������� ��������, ��� ����� ����������� �� ���������-���������� ��� �������� ������!
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
my_gen = (i for i in list_a)
print(sum(my_gen))  # 12
print(sum(my_gen))  # 0

#���������-��������� ����� ���� �����������.
import itertools
inf_gen = (x for x in itertools.count())  # ����������� ��������� �� 0 to �������������!
#������ ��������� � ������ � ������ ������������, ��� ��� ��� �� ���������� ������������� ������� ����� ��� �� ������������ �����.

#� ���������-���������� �� ��������� �����!
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
my_gen = (i for i in list_a)
my_gen_sliced = my_gen[1:3]
# TypeError: 'generator' object is not subscriptable

#----------------------------------------------

#----------------------------------------------
#----------------------------------------------
#----------------------------------------------
#----------------------------------------------
#----------------------------------------------
#----------------------------------------------
