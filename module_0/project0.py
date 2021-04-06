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

#------------------------------------------
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
#----------------------------------------
score_game(game_core_v3)
#¬аш алгоритм угадывает число в среднем за 6 попыток