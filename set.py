L = [1,1,2,3,2]

b = set(L)

print(b)
# {1,2,3}
b_list = list(b)

print(b_list)
# [1,2,3]

# ����� ������� �������� ���������� �������� � ������
c = list(set(L))

print(c)
# [1,2,3]

#�������� ���������, ������� �� ���� ��������� ����� � ������� ���������� ���������� ��������.
i_text = '����� �������� ������������ �����'
print (set(i_text)) 
o_text = list(set(i_text))

# ������� ���������� ���������� �������� � ������.
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
#set.union(other)	�����������	���������� ���������, ��������� �� ��������� set � other.
#set.intersection(other)	�����������	���������� ���������, ��������� �� ���������, ������� ����������� � � set, � � other.
#set.difference(other)	��������	���������� ��������� ��������� set, ������� �� ����������� � other.
#set.symmetric_difference(other)	������������ ��������	���������� ��������� ���������, ������������� � ����� �� ��������, �� �� � ����� ������������.
#----------------------------------------------

# �������������� ���� ��������� ������ �������� ��������� ��������, ������� ����������� � ���� ������� ������������.
a = input("������� ������ ������: ")
b = input("������� ������ ������: ")

a_set, b_set = set(a), set(b) # ���������� ������������� ������������

a_and_b = a_set.intersection(b_set)

print(a_and_b)
#-----------------------------------------------

#�������� ���������, ������� �� ���� �������� ��� ������������������ ����� �����, � ���������� ������ ���������, 
#������������� ������ � ����� �� �������������������. ����� �������� ��� ����������� �� ������������? 
#������� ������ �������� ������ ��� ������.

#symmetric_difference
 
#�������� ����� � ������� ����������� ����� ������, ������� ������� ��������� �� ����������� �������, 
#���� �� ���� �������� ��� ������������������ �����:

1 2 3 4 5 6 7 8
2 4 6 8 10 12

1 3 5 7 10 12


