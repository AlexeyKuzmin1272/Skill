def score_game(game_core):
    '''��������� ���� 1000 ���, ����� ������, ��� ������ ���� ��������� �����'''
    count_ls = []
    np.random.seed(1)  # ��������� RANDOM SEED, ����� ��� ����������� ��� �������������!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"��� �������� ��������� ����� � ������� �� {score} �������")
    return(score)

#------------------------------------------
def game_core_v3(number):
    '''���������� ����� ������� �������: ���� �� ������� �������� �������� ��������� [0,max_value]. 
       ���������� �������� ���������� � ���������� ���������.
       ���� ���� ������ �������� ��������, �� ����� �������������� � ������ �������� ���������, ����� � �� ������
       ������� ��������� ���������� ����� � ���������� ����� �������'''
    #print('�������� '+str(number))
    
    count     = 1
    max_value = 100 # ������������ �����, ������� ����� ���� ��������
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
    return(count) # ����� �� �����, ���� �������
#----------------------------------------
score_game(game_core_v3)
#��� �������� ��������� ����� � ������� �� 6 �������