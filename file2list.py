math = []

f = open('StudentsPerformance.csv')

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        mark = int(info[5][1:-1])
        math.append(mark) 
math_avg = sum(math)/len(math)
print (math_avg)
        
above_avg = 0
for mark in math:
    if mark > math_avg:
        above_avg += 1
print(above_avg / 1000)


#------------
import re
pattern = re.compile('\d+')

exams = []

f = open('StudentsPerformance.csv')

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        new_line = []
        for item in info:
            if pattern.search(item) != None:
                new_line.append(int(pattern.search(item)[0]))
            else:
                new_line.append(item[1:-1])
        exams.append(new_line)
print(exams)

#---------------------------------------------------------------------------------

#Вычислите средний балл абитуриентов на экзамене по чтению (reading score).
#Введите ответ в виде одного числа. Не округляйте полученное значение.

read = []

f = open('StudentsPerformance.csv')

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        mark = int(info[6][1:-1])
        read.append(mark) 

f.close()

#Вычислите средний балл абитуриентов на экзамене по чтению (reading score).
#Введите ответ в виде одного числа. Не округляйте полученное значение.

girls_read = []

f = open('StudentsPerformance.csv')

for line in f:
    info = line.split(',')
    if info[0][1:-1] == 'female' and info[0] != '"gender"':
        #print (info[0]+' '+info[6][1:-1])
        mark = int(info[6][1:-1])
        girls_read.append(mark) 
    else:
        continue

f.close()
girls_avg = sum(girls_read)/len(girls_read)
print (round(girls_avg, 3))

#Сколько абитуриентов получили на экзамене по письму (writing score) оценку выше 90?
wr = []

f = open('StudentsPerformance.csv')

for line in f:
    info = line.split(',')
    if info[0] != '"gender"':
        #print(info[7][1:-2])
        mark = int(info[7][1:-2])
        wr.append(mark) 
    else:
        continue

f.close()

wr_avg = 90 #sum(wr)/len(wr)
cnt = 0

print(c)

for c in wr:
    if c > wr_avg:
        #print(c)
        cnt += 1
        
print (cnt)

#Сколько процентов абитуриентов, получивших на экзамене по письму (writing score) оценку более 90, 
#хорошо пообедали перед экзаменом (lunch = standard)?
#Введите ответ в виде дробного числа без знака процента, округлив до первого знака после запятой.

wr = []

f = open('StudentsPerformance.csv')
dinned = 0
for line in f:
    info = line.split(',')
    if info[0] != '"gender"':
        #print(info[7][1:-2])
        mark = int(info[7][1:-2])
        if mark > 90:
            wr.append(mark) 
            if info[3][1:-1] == 'standard':
                dinned += 1 
    else:
        continue

f.close()

print('Количество абитуриентов, получившх бльше 90 баллов по письму: '+ str(len(wr)))
print('Количество хорошо пообедавших абитуриентов, получившх бльше 90 баллов по письму: ',dinned)
print ('Доля хорошо пообедавших абитуриентов из получившх бльше 90 баллов по письму: ',round(dinned/len(wr)*100, 1), '%') 
