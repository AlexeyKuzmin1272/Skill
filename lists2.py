rabbits = ['�����', '������', '������', '������', '������', '�������', '������', '����']
rabbits[0:7:2]
rabbits[:7:2]
rabbits[0::2]
rabbits[::2]
rabbits[7::-2]
rabbits[:0:-2]
rabbits[::-2]

sparta = ['������', '������', '�������', '������', '������', 
          '������', '��������', '�������', '��������', '�������']
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

my_list = ['�����', '����', '��������', '�����', '�����']
my_list.sort(reverse = True)
print(my_list)


salary = [100000, 45000, 78000, 29000, 55000, 60000, 55000]
print(min(salary)) 
print(max(salary)) 
print(salary.count(55000))


names = ['������', '����', '���������', '�������', '����', '����������', '�����', '�����']
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



fruits = '������ ����� �������� �������� ����� ������� ����� ������'.split()
my_list = []
for fruit in fruits:
    my_list.append(fruit[0])
my_list.sort()
print(fruits)
print(my_list)


#�������� ���������, ������� ������ ������, ���������� �����, ������� ��� ����� � ��������� �� 1 �� 50. 
#������� ����� ��������� ����� ������. ��������� ���������� ��������� � ���������� � ������ result.
a_list = []
for n in range(1,51):
    if n % 3 == 0:
        #print(n)
        a_list.append(n)
#print(a_list)
result=sum(a_list)
print(result)



#�������� ���������, ������� ������ ������ my_list, ���������� ����� ���� �� ������ raw_list (��� � ������ ����), 
#� ������� ����� ������������ � ������������� ��������� ������ ������ (my_list). 
#��������� ���������� (����� ������������ � ������������� ��������� ������ my_list) ��������� ���������� result.

raw_list = ['����������', '�����', '�������', '������', '�������', '�����', '�������']
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


#��� ������ raw_list (���������� ������ ��������� � ������ ����). 
#������� ����������� (x_min) � ������������ (x_max) �������� ��������� ������� ������.
#�������� ����� ������ my_list, ��������� �� ��������� ������ raw_list, ���������� �� x_min, 
#���� ������� �������� ������ ������, � �� x_max, � ������ ���� ������� ��������.

#������� ������������ �������� ������ my_list. ��������� ��������� ���������� result.

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

#���� ���������� ����������� ��������� �������� �� ������ (���� 'source') � ����� �������� ('cost').
#�������� ���, ������� ���� ����������� �������� ����� cost � ���� �������. 

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

#��������� ���� while, ������� ������ ����� �����, ������� �� ���������� � ������.
a = 0
b = 0

while id(a) == id(b):
    a += 1
    b += 1

print(a)
#257

#--------------------------
# ���� �� ��������� � ��� ���������� ���������� ����� �����, �� ��� ���������� ����� ����� � ���� �������: 
#�� �������� ����� (��������� ����� ==), � 
#��� ��������� �� ���������� ������� (��������� ����� is).

a = 42
b = 42

print(a == b)
# True

print(a is b)
# True

#������, ���� �� ��������� �� �� �����, �� � �������, ������������ �������, ��������� � �������, �� ��������� �������� ��������� ����.

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
#����� �������� ������ �������� �������, ������ ����� ����������:
M = L.copy()

print(M is L)
# False
#--------------------

shopping_center = ("�������", "�����-���������", "��������� ��., 30", ["H&M", "Zara"])

shopping_center[-1].append("Uniqlo")

print(shopping_center)
# ('�������', '�����-���������', '��������� ��., 30', ['H&M', 'Zara', 'Uniqlo'])


