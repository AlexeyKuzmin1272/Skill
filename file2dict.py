students = {}

f = open('StudentsPerformance.csv')

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        ethnicity = info[1][1:-1]
        if ethnicity in students:
            students[ethnicity] += 1
        else:
            students[ethnicity] = 1
print(students)            
for group, number in students.items():
    print (group, number)

f.close() 
-------------------------------

students = {}

f = open('StudentsPerformance.csv')

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        ethnicity = info[1][1:-1]
        parents = info[2][1:-1]
        if ethnicity in students:
            if parents in students[ethnicity]:
                students[ethnicity][parents] += 1
            else:
                students[ethnicity][parents] = 1
        else:
            students[ethnicity] = {}
            students[ethnicity][parents] = 1  

f.close()
print(students)
-----------------

#Сколько мальчиков хорошо пообедали перед экзаменом (lunch = standard)?
students = {}

f = open('StudentsPerformance.csv')

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        gender  = info[0][1:-1]
        lunched = info[3][1:-1] 
        
        if gender in students:
            if lunched in students[gender]:
                students[gender][lunched] += 1
            else:
                students[gender][lunched]  = 1
        else:
            students[gender] = {}
            students[gender][lunched] = 1  

f.close()
print(students)
print(students['male']['standard'])
--------------------------------------------

#Сколько мальчиков закончили подготовительные курсы (test preparation course = completed)?
students = {}

f = open('StudentsPerformance.csv')

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        gender  = info[0][1:-1]
        completed = info[4][1:-1]
        
        if gender in students:
            if completed in students[gender]:
                students[gender][completed] += 1
            else:
                students[gender][completed]  = 1
        else:
            students[gender] = {}
            students[gender][completed] = 1  

f.close()
print(students)
print(students['male']['completed'])
--------------------------------

#У скольких девочек родители имеют степень магистра (parental level of education = master's degree)?
students = {}

f = open('StudentsPerformance.csv')

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        gender  = info[0][1:-1]
        level = info[2][1:-1]
        
        if gender in students:
            if level in students[gender]:
                students[gender][level] += 1
            else:
                students[gender][level]  = 1
        else:
            students[gender] = {}
            students[gender][level] = 1  

f.close()
print(students)
print(students['female']['master\'s degree'])
---------------------------

#Сколько абитуриентов, относящихся к этнической группе С, закончили подготовительные курсы?
students = {}
l_x = 1
l_y = 4

f = open('StudentsPerformance.csv')

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        x = info[l_x][1:-1]
        y = info[l_y][1:-1]
        
        if x in students:
            if y in students[x]:
                students[x][y] += 1
            else:
                students[x][y]  = 1
        else:
            students[x] = {}
            students[x][y] = 1  

f.close()
print(students)
print(students['group C']['completed'])

------------------

#Сколько девочек, родители которых имеют степень магистра, набрали по математике больше 90 баллов?
students = {}
l_x = 0
l_y = 2
l_z = 5
l_word = {
    0: 'девочек', 
    1: 'девочка', 
    2: 'девочки', 
    3: 'девочки', 
    4: 'девочки', 
    5: 'девочек', 
    6: 'девочек', 
    7: 'девочек', 
    8: 'девочек', 
    9: 'девочек'
}

l_cnt = 0

f = open('StudentsPerformance.csv')

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        x = info[l_x][1:-1]
        y = info[l_y][1:-1]
        z = info[l_z][1:-1]
        
        if x in students:
            if y in students[x]:
                if z in students[x][y]:
                    students[x][y][z] += 1
                else:
                    students[x][y][z] = 1
            else: 
                students[x][y] = {}     
        else:
            students[x] = {}
            students[x][y] = {}  
            students[x][y][z] = 1  

f.close()
#print(students)
print(students['female']['master\'s degree'])
for  group, number in students['female']['master\'s degree'].items():
    #print(group, number)
    if int(group) > 90:
        l_cnt = l_cnt + number
        
print ( str(l_cnt) + ' ' + l_word[l_cnt % 10]+', родители которых имеют степень магистра, набрали по математике больше 90 баллов')        

---------------	
#Дана строковая переменная с именем string, содержащая одно слово на неизвестном языке. 
#Напишите код, с помощью которого можно перевернуть эту переменную задом наперёд, т.е. получить слово, 
#которое получается при чтении исходного слова справа налево.
#\n                                          

string='test'
for l in basic_word:
	inverted_word = l+inverted_word
print(inverted_word)

string[::-1]

-----------------
#Какой средний балл, полученный мальчиками на экзамене по чтению? Ответ округлите до трёх цифр после запятой.

students = {}
l_x = 0
l_y = 6

l_avg = 0
l_sum = 0
l_cnt = 0

f = open('StudentsPerformance.csv')

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        x = info[l_x][1:-1]
        y = info[l_y][1:-1]
        #print (x+', '+y)
        
        if x in students:
            if y in students[x]:
                students[x][y] += 1
            else: 
                students[x][y] = 1     
        else:
            students[x] = {}
            students[x][y] = 1  

f.close()
for m in students:
    if m == 'male':
        #print (students[m])
        #print ('-----------------')
        
        for mark, cnt in students[m].items():
            #print(mark, cnt)
            l_sum = l_sum + int(mark) * int(cnt)
            l_cnt = l_cnt + cnt
print (l_sum)            
print (l_cnt)            
print (round(l_sum/l_cnt, 3))
            
#print (students)
------------------------------------------------------------------------

#Какой средний балл на экзамене по чтению набрали ученики, набравшие максимальный балл на экзамене по математике? 
#Ответ округлите до трёх цифр после запятой.

students = {}
l_x = 5 # математика
l_y = 6 # чтение

l_math_max = 0

l_avg = 0
l_sum = 0
l_cnt = 0

f = open('StudentsPerformance.csv')

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        x = int(info[l_x][1:-1])
        y = int(info[l_y][1:-1])
        #print (x+', '+y)
        
        if x in students:
            if y in students[x]:
                students[x][y] += 1
            else: 
                students[x][y] = 1     
        else:
            students[x] = {}
            students[x][y] = 1  

f.close()
#print(students[38])
#print(max(students.keys()))

l_math_max = max(students.keys()) # максимальный балл по математике
print (l_math_max)
print (students[l_math_max])

for mark, cnt in students[l_math_max].items():
    #print(mark, cnt)
    l_sum = l_sum + int(mark) * int(cnt)
    l_cnt = l_cnt + cnt

print (l_sum)            
print (l_cnt)            
print (round(l_sum/l_cnt, 3))

----------------------------

#Какой средний балл на экзамене по письму набрали ученики, которые плохо пообедали перед экзаменом (lunch = free/reduced)? 
#Ответ округлите до двух цифр после запятой.
students = {}
l_x = 3 # lunch
l_y = 7 # письмо
l_lunched = 'free/reduced'

l_math_max = 0

l_avg = 0
l_sum = 0
l_cnt = 0

f = open('StudentsPerformance.csv')

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        x = info[l_x][1:-1]
        y = info[l_y][1:-2]
        #print (x+', '+y)
        
        if x in students:
            if y in students[x]:
                students[x][y] += 1
            else: 
                students[x][y] = 1     
        else:
            students[x] = {}
            students[x][y] = 1  

f.close()
print(students[l_lunched])

for mark, cnt in students[l_lunched].items():
    l_sum = l_sum + int(mark) * int(cnt)
    l_cnt = l_cnt + int(cnt)

print(l_sum)
print(l_cnt)
print (round(l_sum/l_cnt, 2))

