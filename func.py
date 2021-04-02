def linear_solve(a, b):
    return b / a

# 2*x = 9
print(linear_solve(2, 9))
#------------------------------------
def linear_solve(a, b):
    if a: # ������, ��� 0 ���������������� ��� False, ����� True
        return b / a
    else:
        return "��� ������"

print(linear_solve(0,1))
#------------------------------------
def linear_solve(a, b):
    if a: 
        return b / a
    elif not a and not b: # ����� ���������� ����� � ���������� ����������
        return "����������� ���������� ������"
    else:
        return "��� ������"
print(linear_solve(0,0))
#------------------------------------
#���������� ������� quadratic_solve(a, b, c), ������������ ���� ������������ ������ � ������ �������������� �������������.
def quadratic_solve(a, b, c):
    if D (a, b) < 0:
        print ('��� ������������ ������')
#------------------------------------
#���������� ������� quadratic_solve(a, b, c), ������������ ���� ������������ ������ � ������ �������������� �������������.
#������������ ������� ����� �������, ����� ��� ������� ������������� ������������ �������� ������������� �����.
def quadratic_solve(a, b, c):
    di = D (a, b, c)
    if di < 0:
        return "��� ������������ ������"
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
����������, ��� ��������� ������ �������� �� � ���� ������, � � ���� �������.

M = {'a': 1,
     'b': 0,
     'c': -1}
M.values()
print(quadratic_solve(**M))
#�������� ���������� ������� (**) 
#------------------------------------
#�������� ����������� �������, ��������� ����������� ������� ������ ��� ������������� ������ � ���������� ������� min().
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
#�������� ����������� �������, ������� ��������� ������������� �����. ��������������, ��� ����� �� �������� ����.

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
##����������� ������� equal(N, S), �����������, ��������� �� ����� ���� ����� N � ������ S. 
#��� ��������� ��������� ������� �������� �������� �� ��, ���, ���� S ����� �������������, 
#�� ���������� ����� ������� False.
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
for a in e(): # e() � ���������
    cnt +=1
    if (a - last) < 0.00000000000001: # ����������� �� ��������
        print(a)
        print(cnt)
        break # ����� ���������� �������� � ��������� ����
    else:
        last = a # ����� � ����������� ����� ��������     
#print(last)    
#------------------------------------
USERS = ['admin', 'guest', 'director', 'root', 'superstar']

yesno = input("""������� Y, ���� ������ ��������������, ��� N, 
             ���� ������ ���������� ������ ��� ��������� ������������: """)

auth = yesno == "Y"

if auth:
    username = input("������� ��� username:")

def is_auth(func):
    def wrapper():
        if auth:
            print("������������ �����������")
            func()
        else:
            print("������������ �������������. ������� ��������� �� �����")
    return wrapper

def has_access(func):
    def wrapper():
        if username in set(USERS): #== 'admin' :
            print("������������ ����� ������")
            func()
        else:
            print("������������ �� ����� �������. ������� ��������� �� �����")
    return wrapper

@is_auth
@has_access
def from_db():
    print("some data from database")

from_db()
#------------------------------------
#------------------------------------
#------------------------------------
