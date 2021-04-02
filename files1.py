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
print('Мальчиков: {}, девочек: {}'.format(males, females))

#У скольких абитуриентов родители имеют диплом бакалавра (bachelor's degree)?
#Введите ответ в виде целого числа. При написании кода обратите внимание на использование кавычек/апострофов
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

#Сколько разных вариантов значений встречается в столбце "parental level of education"?
#Сколько разных вариантов значений встречается в столбце "parental level of education"?
#Введите ответ в виде целого числа.
#Подсказка 1: для хранения уникальных вариантов вы можете использовать список.
#Подсказка 2: не забудьте, что первая строка файла содержит заголовки столбцов и не должна учитываться при обработке
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


#Сколько процентов абитуриентов полноценно пообедали перед экзаменом? 
#Иными словами, у скольких процентов абитуриентов значение столбца "lunch" = "standard"?
#Ответ введите в виде десятичной дроби, в качестве разделителя используйте точку. Знак процента вводить не нужно.
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


#Сколько абитуриентов относится к этнической группе "group C"?
#Введите ответ в виде целого числа.
f = open('StudentsPerformance.csv')
groupc_cnt = 0
for l in f:
    info = l.split(',')
    if info[1][1:-1] == 'group C':      
        groupc_cnt += 1
f.close()
print(groupc_cnt)


#Сколько разных этнических групп встречается в файле?
#Введите ответ в виде целого числа.
#Подсказка 1: для хранения уникальных вариантов Вы можете использовать список.
#Подсказка 2: не забудьте, что первая строка файла содержит заголовки столбцов и не должна учитываться при обработке
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

