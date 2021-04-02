f = open('StudentsPerformance.csv') 
for line in f:
         print(line)
f.close()

f = open('StudentsPerformance.csv')
males = 0
females = 0
for line in f:
    info = line.split(',')
    gender = info[0][1:-1]
    if gender == 'female':
        females += 1
    elif gender == 'male':
        males +=1
print('���������: {}, �������: {}'.format(males, females))

#� �������� ������������ �������� ����� ������ ��������� (bachelor's degree)?
#������� ����� � ���� ������ �����. ��� ��������� ���� �������� �������� �� ������������� �������/����������
f = open('StudentsPerformance.csv')
bach_count = 0
for l in f:
    pl_edu = ''
    info = l.split(',')
    if info[2][1:-1] == 'bachelor\'s degree':
        bach_count += 1
    #pl_edu = 
    print(info[2][1:-1])
print(bach_count)
f.close()

#������� ������ ��������� �������� ����������� � ������� "parental level of education"?
#������� ������ ��������� �������� ����������� � ������� "parental level of education"?
#������� ����� � ���� ������ �����.
#��������� 1: ��� �������� ���������� ��������� �� ������ ������������ ������.
#��������� 2: �� ��������, ��� ������ ������ ����� �������� ��������� �������� � �� ������ ����������� ��� ���������
f = open('StudentsPerformance.csv')
lvl = []
for l in f:
    info = l.split(',')
    lvl.append(info[2][1:-1])
f.close()
counter = 0
unique_levels = list(set(lvl))
print(unique_levels)
for i in unique_levels:
    if i != 'parental level of education':
        counter += 1
print (counter)


#������� ��������� ������������ ���������� ��������� ����� ���������? 
#����� �������, � �������� ��������� ������������ �������� ������� "lunch" = "standard"?
#����� ������� � ���� ���������� �����, � �������� ����������� ����������� �����. ���� �������� ������� �� �����.
f = open('StudentsPerformance.csv')
total = 0
lunched = 0
for l in f:
    info = l.split(',')
    if info[3][1:-1] != 'lunch':      
        total += 1
        if info[3][1:-1] == 'standard':
            lunched += 1
print(lunched/total*100)
f.close()


#������� ������������ ��������� � ���������� ������ "group C"?
#������� ����� � ���� ������ �����.
f = open('StudentsPerformance.csv')
groupc_cnt = 0
for l in f:
    info = l.split(',')
    if info[1][1:-1] == 'group C':      
        groupc_cnt += 1
f.close()
print(groupc_cnt)


#������� ������ ���������� ����� ����������� � �����?
#������� ����� � ���� ������ �����.
#��������� 1: ��� �������� ���������� ��������� �� ������ ������������ ������.
#��������� 2: �� ��������, ��� ������ ������ ����� �������� ��������� �������� � �� ������ ����������� ��� ���������
f = open('StudentsPerformance.csv')
egrp = []
for l in f:
    info = l.split(',')
    if info[1][1:-1] != 'race/ethnicity':      
        egrp.append(info[1][1:-1])
f.close()
unique_egrp = list(set(egrp))
print (unique_egrp)
counter = 0
for i in unique_egrp:
    counter += 1
print (counter)        

