import numpy as np
count = 0                           # ������� �������
number = np.random.randint(1,101)   # �������� �����
print ("�������� ����� �� 1 �� 100")
    
while True:                        # ����������� ����
    predict = int(input())         # �������������� �����
    count += 1                     # ������� �������
    if number == predict: break    # ����� �� �����, ���� �������
    elif number > predict: print (f"����������� ����� ������ {predict} ")
    elif number < predict: print (f"����������� ����� ������ {predict} ")
            
print (f"�� ������� ����� {number} �� {count} �������.")    

#--------------------------------------------

number = np.random.randint(1,101)      # �������� �����
print ("�������� ����� �� 1 �� 100")
for count in range(1,101):         # ����� ���������� ������� ��������
    if number == count: break      # ����� �� �����, ���� �������      
    print (f"�� ������� ����� {number} �� {count} �������.")    

#--------------------------------------------

def game_core_v1(number):
    '''������ ��������� �� random, ����� �� ��������� ���������� � ������ ��� ������.
       ������� ��������� ���������� ����� � ���������� ����� �������'''
    count = 0
    while True:
        count+=1
        predict = np.random.randint(1,101) # �������������� �����
        if number == predict: 
            return count # ����� �� �����, ���� �������
        
        
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

score_game(game_core_v1)

#--------------------------------------------

def game_core_v2(number):
    '''������� ������������� ����� random �����, � ����� ��������� ��� ����������� ��� � ����������� �� ����, ������ ��� ��� ������ �������.
       ������� ��������� ���������� ����� � ���������� ����� �������'''
    count = 1
    predict = np.random.randint(1,101)
    while number != predict:
        count+=1
        if number > predict: 
            predict += 1
        elif number < predict: 
            predict -= 1
    return(count) # ����� �� �����, ���� �������

score_game(game_core_v2)

#--------------------------------------------

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

score_game(game_core_v3)  