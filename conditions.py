flower = '����'
color = '����������'
if flower == '����':
    if color == '�����' or color == '�����':
        print ("��� ���������� ��� �����")
    else:
        print ("��� �� ����� ����� �����")
else:
    print ("��� �� ����� ����� �����")

height = 180
weight = 92
color = '�����'
if height > 170 and weight < 80 and color == '�������':
    print ("���� ��������� �������!")
else:
    print ("��������� �������� ���...")


number = 346
if number % 2 == 0 or number % 5 == 0 or number % 173 == 0 or number % 821 == 0:
    print("����, ��� ������ �����")
else:
    print("����, � ���� ��� �� �� �����")


fav_word = '����������'
if fav_word in ["��������", "�����", "����"]:
    print("Python")
elif fav_word in ["����", "�����"]:
    print("C++")
elif fav_word in ["�����","��������"]:
    print("Ruby")
else:
    print("Python")



hour = 18 
minute = 47
dayminutes = hour * 60 + minute
if dayminutes <= 10*60 or dayminutes >= 20*60:
    print("������������� - ����")
elif (dayminutes >= 10*60+30 and dayminutes <= 12*60) or (dayminutes >= 13*60+40 and dayminutes <= 15*60) or (dayminutes >= 18*60 and dayminutes <= 19*60+30):
    print("������������� �����.")
else:     
    print("������������� ��������.")

#------------------------
if some_var is None:
    print("NoneType")
else:
    print(type(some_var))

#------------------------
a = None # ������ ������
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

# ����� a � b - ����������, ������� �� ����� ���������
if a and b : # �������� ���������� ����� ����������
    print("��� ���������� ��������")
    print(a,b)
#--------------------------

# ����� a � b - ����������, ������� �� ����� ���������
if a and b:
    print("��� ���������� ��������")
    print(a,b)
elif a or b:
    print("���� �� ���������� ��������")
    print( a or b ) # ������ �������� ����� ����������, ������� �������� ��������
#----------------------------------------

#  �� ����� ���������, �������� �� ��� �����, 
# ��������� �� � ����������� ���������� (��������, �� 100 �� 999 ������������), 
#�� ��� � ������� �� �� 2 � 3 ������������. 
import locale

locale._override_localeconv["thousands_sep"] = ""
locale._override_localeconv["decimal_point"] = "."

#locale.atof('123456,78')

a = locale.atof(input('������� ����� '))
print(a)
if a == int(a) and a >= 100 and a <= 999 and a % 2 == 0 and a % 3 == 0:
    print ('������� �����������')
else:
    print ('������� �� �����������')
#----------------------------------------
#������������ �������
import locale

locale._override_localeconv["thousands_sep"] = ""
locale._override_localeconv["decimal_point"] = "."

#locale.atof('123456,78')

a = locale.atof(input('������� ����� '))
print(type(a))
if all([type(a) == int,
       100 <= a <= 999,
       a % 2 == 0,
       a % 3 == 0]):
    print ('������� �����������')
else:
    print ('������� �� �����������')

#--------------------------
#�������� ���������, ������� �� ���� ��������� ������������������ ����� ����� � ���������� True, ���� ��� ����� ���������, 
#� False, ���� ���� �� ���� ����� ����� 0.
L = list(map(int, input().split(',')))

print(all(L))

#------------------------------
#�������� ���������, ������� �� ���� ��������� ������������������ ����� ����� � ���������� True, ���� ��� ����� ����� ����, 
#� False, ���� ������� ���� �� ���� ��������� �����. ����������� ������������� ������ ���������� ���������� � ������� all([ ]) � any([ ]).
L = list(map(int, input().split(' ')))
print(any(L))
#------------------------------
