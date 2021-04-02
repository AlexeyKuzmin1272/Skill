a = (1, [2, 3], 4)
print(type(a))   # <type 'tuple'>
b = {a: 1}       # TypeError: unhashable type: 'list'
#-----------------------------------------------
a = {}
print(type(a))     # <class 'dict'>

b = {1, 2, 3}   
print(type(b))     # <class 'set'>

c = {'a': 1, 'b': 2}
print(type(c))     # <class 'dict'>
#-----------------------------------------------
# ������� ������� ������ � ������� (����������� ����� ��������� ����):
my_list = ['a', 'b', 'c', 'd', 'e', 'f']
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
print(my_list)   # ['a', 'b', 'c', 'd', 'e', 'f']
print(my_dict)   # {'a': 1, 'c': 3, 'e': 5, 'f': 6, 'b': 2, 'd': 4}
                 # �� ��������, ��� ������� ��������� � ����������������� ���������� �� �����������.
#-----------------------------------------------
print(len(my_list)) # 6
print(len(my_dict)) # 6 - ��� ������� ���� ����-�������� ��������� ����� ���������. 
print(len('ab c')) # 4 - ��� ������ ��������� �������� 1 ������

#-----------------------------------------------
my_list = ['a', 'b', 'c', 'd', 'e', 'f']
print('a' in my_list)           # True
print('q' in my_list)           # False
print('a' not in my_list)       # False
print('q' not in my_list)       # True
#-----------------------------------------------
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
print('a' in my_dict)               # True - ��� �������� ������ ����� �� ������
print('a' in my_dict.keys())        # True - ���������� ������� ����
print('a' in my_dict.values())      # False - ��� ��� '�' � ����, �� ��������
print(1 in my_dict.values())        # True
#-----------------------------------------------
print(('a',1) in my_dict.items())   # True
print(('a',2) in my_dict.items())   # False
#-----------------------------------------------
#��� ������ ����� ������ �� ������ ���� ������, �� � ���������:

print('ab' in 'abc')    # True
#-----------------------------------------------
for elm in my_dict:
     	# ��� ����� ������ �������, ������������ ������ �����
	# ����������� for elm in my_dict.keys()
     	print(elm)

 for elm in my_dict.values():
     	# ��� ������� ����� ������ ������ �� ���������
     	print(elm)

#�� ���� ����� ����� ���� ����(key) � �������� (value).

for key, value in my_dict.items():
	# ������ �� .items() ���������� ������ (����, ��������), 
	# ������� ������������� ������� ���������� key, value
	print(key, value)
#-----------------------------------------------
#��������� ������: �� ������� ���������� ��������� ��������� � ���� ����� �� ����� �������� �� ���� �� ���������! � 
#��� ��������� �� ������ ��������� �� ������ ������ ������.
#����� ����� �������� �������� �������� ��������, �����, ��������, ����������� ����� ���������:

for elm in list(my_list):
    	# ������ ������ ������� � ��������� �������� � �������� ������ my_list,
    	# ��� ��� �������� ���� �� ��� �����.
#-----------------------------------------------
print(min(my_list))               # a
print(sum(my_dict.values()))      # 21
#-----------------------------------------------
my_list = [1, 2, 2, 2, 2, 3]
print(my_list.count(2))     # 4 ���������� �������� ������� 2
print(my_list.count(5))     # 0 - �� ���� ������ �������� � ��������� ���
#-----------------------------------------------
my_list = [1, 2, 2, 2, 2, 3]
print(my_list.index(2))  # ������ ������� ������ 2 ��������� �� ������� 1 (���������� � ����!)
print(my_list.index(5))  # ValueError: 5 is not in list - ������������� ������� ������ ������!
#-----------------------------------------------
my_set = {1, 2, 3}
my_set_2 = my_set.copy()
print(my_set_2 == my_set)  # True - ��������� ����� - �������� ���������� ��������
print(my_set_2 is my_set)  # False - ��������� �� ��������� - ��� ������ ������� � ������� id

#-----------------------------------------------
my_set = {1, 2, 3}
print(my_set)  # {1, 2, 3}
my_set.clear()
print(my_set)  # set()
#-----------------------------------------------
set_a = {1, 2, 3}              
set_b = {2, 1}                  # ������� ��������� �� �����!
set_c = {4}
set_d = {1, 2, 3}

print(set_a.isdisjoint(set_c))  # True - ��� ����� ���������
print(set_b.issubset(set_a))    # True  - set_b ������� ������ � set_a, ������ set_b - ������������
print(set_a.issuperset(set_b))  # True - set_b ������� ������ � set_a, ������ set_a - ������������
#-----------------------------------------------
my_tuple = ('a', 'b', 'a')
my_list = list(my_tuple)
my_set = set(my_tuple)		        # ������ ������� � ��������� ���������!
my_frozenset = frozenset(my_tuple)      # ������ ������� � ��������� ���������!
print(my_list, my_set, my_frozenset)    # ['a', 'b', 'a'] {'a', 'b'} frozenset({'a', 'b'})
#-----------------------------------------------
my_keys = ('a', 'b', 'c')
my_values = [1, 2]      # ���� ���������� ��������� ������ - 
		        # ����� ���������� ���� ������� �� ���� - ������ ���������
my_dict = dict(zip(my_keys, my_values))
print(my_dict)         # {'a': 1, 'b': 2}
#-----------------------------------------------
my_tuple = ('a', 'b', 'c')
my_str = ''.join(my_tuple)
print(my_str)       # abc
#-----------------------------------------------
my_list = [1, [2, 3], 4]
my_set = set(my_list)   # TypeError: unhashable type: 'list'

#-----------------------------------------------
my_2lvl_list = [[1, 2, 3], ['a', 'b', 'c']]
print(my_2lvl_list[0])      # [1, 2, 3] - ������ ������� � ������ ��������� ������
print(my_2lvl_list[0][0])   # 1 � ������ ������� ������� ���������� ������
print(my_2lvl_list[1][-1])  # � � ��������� ������� ������� ���������� ������
#-----------------------------------------------
my_list = [1, 2, 3, [4, 5]]
my_list[0] = 10
my_list[-1][0] = 40
print(my_list)      	# [10, 2, 3, [40, 5]]

#����������: ��� ������ ����������, ������� ��� ������ ������������ � ������, ������ ����� ������� �������� ������� �� �������������� ������.
my_list = [1, 2, 3, 4, 5]
my_list[5] = 6      # IndexError: list assignment index out of range
#-----------------------------------------------
person = ('Alex', 'Smith', "May", 10, 1980)
NAME, BIRTHDAY = slice(None, 2), slice(2, None)       
	# ������ ���������� ����������� �����
        # ������ ��������� � ���������� ������� ��������� ���������������� �������
print(person[NAME])      # ('Alex', 'Smith')
print(person[BIRTHDAY])  # ('May', 10, 1980)

my_list = [1, 2, 3, 4, 5, 6, 7]
EVEN = slice(1, None, 2)
print(my_list[EVEN])     # [2, 4, 6]
#-----------------------------------------------
my_list = [1, 2, 3, 4, 5]
# my_list[1:2] = 20     # TypeError: can only assign an iterable
my_list[1:2] = [20]     # ��� ������ ��� ��������
print(my_list)          # [1, 20, 3, 4, 5]
#-----------------------------------------------
my_list = [1, 2, 3, 4, 5]
my_list[1:3] = [20, 30]
print(my_list)          # [1, 20, 30, 4, 5]
my_list[1:3] = [0]      # ��� ������� �������� ��� �������� �� ����
print(my_list)          # [1, 0, 4, 5]
my_list[2:] = [40, 50, 60]   # ��� ��� �������� �� ���
print(my_list)               # [1, 0, 40, 50, 60]

#����� ������ ������� ����� ������������������

my_list = [1, 2, 3, 4, 5]
my_list[:2] = []    # ��� del my_list[:2]
print(my_list)      # [3, 4, 5]
#-----------------------------------------------
#��������� � ��������������� ������� ��������� �������� ������:

my_list = [1, 2, 3, 4, 5]
print(my_list[-10])       # IndexError: list index out of range
print(my_list[10])        # IndexError: list index out of range

#� � ������ ������ ������ ����� �� ������� ��������� ������� ������ �� ����������:

my_list = [1, 2, 3, 4, 5]
print(my_list[0:10])      # [1, 2, 3, 4, 5] � ���������� � �������� ���������
print(my_list[10:100])	  # [] - ����� ��������� ��� � ������� ������ ���������
print(my_list[10:11])     # [] - ��������� 1 ������������� ������� - ������ ���������, ��� ������
#-----------------------------------------------
my_list = [2, 5, 1, 7, 3]
my_list_sorted = sorted(my_list)
print(my_list_sorted)       # [1, 2, 3, 5, 7]

my_set = {2, 5, 1, 7, 3}
my_set_sorted = sorted(my_set, reverse=True)
print(my_set_sorted)        # [7, 5, 3, 2, 1]
#-----------------------------------------------
my_files = ['somecat.jpg', 'pc.png', 'apple.bmp', 'mydog.gif']
my_files_sorted = sorted(my_files, key=len)
print(my_files_sorted)      # ['pc.png', 'apple.bmp', 'mydog.gif', 'somecat.jpg']
#-----------------------------------------------
my_list = [2, 5, 1, 7, 3]
my_list_sorted = reversed(my_list)
print(my_list_sorted)           # <listreverseiterator object at 0x7f8982121450>
print(list(my_list_sorted))     # [3, 7, 1, 5, 2]
print(my_list[::-1])            # [3, 7, 1, 5, 2] - ��� �� ��������� � ������� �����
#-----------------------------------------------
my_list = [2, 5, 1, 7, 3]
my_list.sort()
print(my_list)          # [1, 2, 3, 5, 7]

#-----------------------------------------------
my_list = [2, 5, 1, 7, 3]
my_list = my_list.sort()
print(my_list)          # None

#-----------------------------------------------
my_dict = {'a': 1, 'c': 3, 'e': 5, 'f': 6, 'b': 2, 'd': 4}
mysorted = sorted(my_dict)
print(mysorted)           # ['a', 'b', 'c', 'd', 'e', 'f']
mysorted = sorted(my_dict.items())
print(mysorted)           # [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6)]
mysorted = sorted(my_dict.values())
print(mysorted)           # [1, 2, 3, 4, 5, 6]

#-----------------------------------------------
population = {"Shanghai": 24256800, "Karachi": 23500000, "Beijing": 21516000, "Delhi": 16787941}
# ����������� �� ����������� ���������:
population_sorted = sorted(population.items(), key=lambda x: x[1])
print(population_sorted)
# [('Delhi', 16787941), ('Beijing', 21516000), ('Karachi', 23500000), ('Shanghai', 24256800)]
#-----------------------------------------------
shop = [('�������', 1200), ('�����', 1000), ('�����', 300),
        ('������', 100), ('�����', 1500), ('����', 12000),
        ('����', 2000), ('�����', 200), ('�����', 2700)]
for det, price in shop:
    print('{:<10} ����: {:>5}�.'.format(det, price))

print('--------------------------------------')   

def prepare_item(item):
    return (item[0], -item[1])

# ������������� �� ������� �������
shop.sort(key=prepare_item)

for det, price in shop:
    print('{:<10} ����: {:>5}�.'.format(det, price))

print('--------------------------------------')   
def prepare_item(item):
    return (item[1])

# ������������� �� �������� �������
shop.sort(key=prepare_item)

for det, price in shop:
    print('{:<10} ����: {:>5}�.'.format(det, price))

#-----------------------------------------------
#-----------------------------------------------
#����� �� ������� ����������� �������, ������ ������������� ��������� �������, ���� �� ������� ����� �������� 
#� �������������� ������-�������.
shop = [('�������', 1200), ('�����', 1000), ('�����', 200),
        ('������', 100), ('�����', 1500), ('����', 12000),
        ('����', 200), ('�����', 200), ('�����', 2700)]

shop.sort(key=lambda x: x[0], reverse=True)
shop.sort(key=lambda x: (-x[1])) #shop.sort(key=lambda x: (x[0], -x[1]))

for det, price in shop:
    print('{:<10} ����: {:>5}�.'.format(det, price))
#-----------------------------------------------
str1 = 'abc'
str2 = 'de'
str3 = str1 + str2
print(str3)         # abcde

tuple1 = (1, 2, 3)
tuple2 = (4, 5)
tuple3 = tuple1 + tuple2
print(tuple3)       # (1, 2, 3, 4, 5)
#-----------------------------------------------
a = [1, 2, 3]
b = [4, 5]
c = a + b           
print(a, b, c)      # [1, 2, 3]  [4, 5]  [1, 2, 3, 4, 5]
#-----------------------------------------------
a = [1, 2, 3]
b = [4, 5]
c = a + [b]
print(a, b, c)     # [1, 2, 3]  [4, 5]  [1, 2, 3, [4, 5]]
#-----------------------------------------------
a, b = [1, 2, 3], [4, 5]
c = [*a, *b]  # �������� �� ������ ������ 3.5 � ����
print(c)      # [1, 2, 3, 4, 5]
#-----------------------------------------------
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)        	# {'a': 1, 'c': 3, 'b': 2, 'd': 4}

#-----------------------------------------------
#� ������ 3.5 �������� ����� ����� ������� ������:

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {**dict1, **dict2}
print(dict3)        	# {'a': 1, 'c': 3, 'b': 2, 'd': 4}
#-----------------------------------------------
#����������� (union):

c = a.union(b)     # c = b.union(a) ���� ����� �� ���������	
# c = a + b        # ������� ����������� ���������� + �� ��������
		   # TypeError: unsupported operand type(s) for +: 'set' and 'set'
c = a | b          # �������������� ����� ������ �����������
print(c)	   # {'a', 'c', 'b'}
#-----------------------------------------------
#����������� (intersection):

c = a.intersection(b)    # c = b.intersection(a) ���� ����� �� ���������
c = a & b                # �������������� ����� ������ �����������
print(c)                 # {'b'}

#����������� ����� 2-� �������� �����:
a = {'a', 'b'}
b = {     'b', 'c'}
c = {    'b', 'd'}
d = a.intersection(b, c)	# ������ ������� ������
d = set.intersection(a, b, c)   # ������ ������� ������ (����� ���������)
print(d)                        # {'b'}
#-----------------------------------------------
������� (difference) � ��������� ������� �� ����, ����� ��������� �� ������ ��������:

c = a.difference(b)      # c = a - b ������ ������ ������ ������ ��� �� ���������
print(c)                 # {'a'}
c = b.difference(a)      # c = b - a ������ ������ ������ ������ ��� �� ���������
print(c)                 # {'c'}
#-----------------------------------------------
#������������ ������� (symmetric_difference) ��� ������ ���� �������� ��������������� ����������� � 
#�������� �������� �� ����� �������� ������� �� ������������, �� ���� ��� ����� �����������:

c = b.symmetric_difference(a)   
# c = a.symmetric_difference(b)       # ���� ����� �� ���������
c = b ^ a                             # �������������� ����� ������ ������������ �������
print(c)        		      # {'a', 'c'}
#-----------------------------------------------
a.extend(b)    # a += b ������������ a.extend(b)
print(a, b)    # [1, 2, 3, 4, 5]  [4, 5]
#-----------------------------------------------
#��������� ��� �������� ������� ������ � ��������� ������� � �������� ������� ������ ������� .extend():
a = [1, 2, 3]
b = [4, 5]
a.extend(b)    # a += b ������������ a.extend(b)
print(a, b)    # [1, 2, 3, 4, 5]  [4, 5]
#-----------------------------------------------
#��������� ������ ������ ��� ���� ������� � ���������� ������� ������ ������� .append():
a = [1, 2, 3]
b = [4, 5]

a.append(b)    # a += [b] ������������ a.append(b)
print(a, b)    # [1, 2, 3, [4, 5]]  [4, 5]
#-----------------------------------------------
#��� ��������� ������� � ���������� ��������� ������� ������� ������������ ����� .update().
#�������� ��������: ��� ����������� ������ ������� ��� ���� ����������� ��������:

dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 100, 'c': 3, 'd': 4}
dict1.update(dict2)
print(dict1)        # {'a': 100, 'c': 3, 'b': 2, 'd': 4}
#-----------------------------------------------
#.difference_update()

a = {'a', 'b'}
b = {     'b', 'c'}
a.difference_update(b)
print(a, b)         # {'a'} {'b', 'c'}
a = {'a', 'b'}
b = {     'b', 'c'}
b.difference_update(a)
print(a, b)     
#-----------------------------------------------
#intersection_update()

a = {'a', 'b'}
b = {     'b', 'c'}
a.intersection_update(b)
print(a, b)         # {'b'} {'b', 'c'}

a = {'a', 'b'}
b = {     'b', 'c'}
b.intersection_update(a)
print(a, b)         # {'b', 'a'} {'b'}
#-----------------------------------------------
#.symmetric_difference_update()

a = {'a', 'b'}
b = {     'b', 'c'}
a.symmetric_difference_update(b)    
print(a, b)         # {'c', 'a'} {'c', 'b'}

a = {'a', 'b'}
b = {     'b', 'c'}
b.symmetric_difference_update(a)
print(a, b)         # {'a', 'b'} {'c', 'a'}
#-----------------------------------------------
������� ������������� ������ .insert(index, element)
my_list = [1, 2, 3]
my_list.insert(0, 0)    # index = 0 - ��������� � ������
print(my_list)          # [0, 1, 2, 3]

my_list.insert(10, 4)   # ������ ������� �� ������� ������ -  ������ ������� � �����
print(my_list)          # [0, 1, 2, 3, 4]

my_list.insert(-10, -1) # ������ ������� �� ������� � ����� - ������� � ������
print(my_list)          # [-1, 0, 1, 2, 3, 4]

my_list = [1, 2, 3]
my_list.insert(1, 1.5)  # ������� ����� 1 � 2 (���������� � ����!)
# �� ���� ����������� �� ������� � ��������� ��������, � �� �������� ��� �� ��� ���� 
# � �� ��� ������ - ���������� �� 1 ������ ������
print(my_list)          # [1, 1.5, 2, 3]
#-----------------------------------------------
#������ ������������ ��������� � ���� �� �� ������ � �� ������� ����� ������!

str1 = 'abc'
print(str1, id(str1))       # abc 140234080454000
str1 += 'de'
print(str1, id(str1))       # abcde 140234079974992 - ��� ����� ������, � ������ id!
#-----------------------------------------------
#������ ���� � ����� ������� ����������� ��������.

str1 = 'abc'
str2 = str1
print(str1 is str2)       # True - ��� ��� ������ �� ���� � ��� �� ������!
str1 += 'de'              # ������ ���������� str1 ��������� �� ������ ������!
print(str1 is str2)       # False - ������ ��� ��� ������ �������!
print(str1, str2)         # abcde abc - ������ ��������
#-----------------------------------------------
#������ �������� � ��� ���� ���� ����� ������������, ����� �� ��������� ��������� ������! 
#�������� ������ ������ � �������� �� �������� ����:

list1 = [1, 2, 3]
list2 = list1
print(list1 is list2)     # True - ��� ��� ������ �� ���� � ��� �� ������!
# � ������ ����������, ��������� ��� �����:
list1 += [4]
print(list1, list2)       # [1, 2, 3, 4] [1, 2, 3, 4] 
# ���������� �������� ����� ����������, ��� ��� ��� ���������� ��������� �� ���� ������!
#-----------------------------------------------
#� ���� ����� ����������� �����, � ������� ����� �������� ��������?

list1 = [1, 2, 3]
list2 = list(list1)       # ������ ������ �����������
list3 = list1[:]          # ������ ������ �����������
list4 = list1.copy()      # ������ ������ ���������� - ������ � Python 3.3+
print(id(list1), id(list2), id(list3), id(list4))      
# ��� 4 id ������, ��� ������ ��� �� ������� 4 ������ �������

list1 += [4]              # ������ �������� ������
print(list1, list2, list3, list4)       # [1, 2, 3, 4] [1, 2, 3] [1, 2, 3] [1, 2, 3]  
# ��� �� � ������ - ������� �������� ������, ��� ����� �������� �� ���������
#-----------------------------------------------

#-----------------------------------------------
#-----------------------------------------------
#-----------------------------------------------
#-----------------------------------------------
#-----------------------------------------------
#-----------------------------------------------
#-----------------------------------------------
#-----------------------------------------------
#-----------------------------------------------
#-----------------------------------------------
#-----------------------------------------------
#-----------------------------------------------
#-----------------------------------------------
#-----------------------------------------------
