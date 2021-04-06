import numpy as np
count = 0                           # счетчик попыток
number = np.random.randint(1,101)   # загадали число
print ("«агадано число от 1 до 100")
    
while True:                        # бесконечный цикл
    predict = int(input())         # предполагаемое число
    count += 1                     # плюсуем попытку
    if number == predict: break    # выход из цикла, если угадали
    elif number > predict: print (f"”гадываемое число больше {predict} ")
    elif number < predict: print (f"”гадываемое число меньше {predict} ")
            
print (f"¬ы угадали число {number} за {count} попыток.")    

#--------------------------------------------

number = np.random.randint(1,101)      # загадали число
print ("«агадано число от 1 до 100")
for count in range(1,101):         # более компактный вариант счетчика
    if number == count: break      # выход из цикла, если угадали      
    print (f"¬ы угадали число {number} за {count} попыток.")    

#--------------------------------------------

def game_core_v1(number):
    '''ѕросто угадываем на random, никак не использу€ информацию о больше или меньше.
       ‘ункци€ принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count+=1
        predict = np.random.randint(1,101) # предполагаемое число
        if number == predict: 
            return count # выход из цикла, если угадали
        
        
def score_game(game_core):
    '''«апускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"¬аш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core_v1)

#--------------------------------------------

def game_core_v2(number):
    '''—начала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       ‘ункци€ принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1,101)
    while number != predict:
        count+=1
        if number > predict: 
            predict += 1
        elif number < predict: 
            predict -= 1
    return(count) # выход из цикла, если угадали

score_game(game_core_v2)

#--------------------------------------------

def game_core_v3(number):
    '''»спользуем метод делени€ пополам: берЄм за искомое значение середину интервала [0,max_value]. 
       ѕолученное значение сравниваем с загаданным значением.
       ≈сли ключ меньше значени€ середины, то поиск осуществл€етс€ в первой половине элементов, иначе Ч во второй
       ‘ункци€ принимает загаданное число и возвращает число попыток'''
    #print('«агадано '+str(number))
    
    count     = 1
    max_value = 100 # максимальное число, которое может быть загадано
    min_value = 1
    predict   = (max_value+1 - min_value)//2
    
    while number != predict:
        count += 1
        
        if number > predict: 
            min_value = predict
        else: 
            max_value = predict
            
        predict = min_value + (max_value+1 - min_value)//2    
        
        if count > 100: 
            break
    return(count) # выход из цикла, если угадали

score_game(game_core_v3)  