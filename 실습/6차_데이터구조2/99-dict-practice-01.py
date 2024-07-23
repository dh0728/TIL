# 각 혈액형의 인원수를 계산하는 딕셔너리를 생성하기.
blood_types = ['A', 'B', 'O', 'AB', 'A', 'O', 'B', 'A', 'AB', 'O', 'A', 'B']


# 1. [] 표기법을 사용한 방법
def count_blood_types(blood_types):
    # 방법1
    # new_dict= dict({'A':0 ,'B':0, 'O':0 , 'AB':0})
    # for k in new_dict.keys():
    #     new_dict[k]=blood_types.count(k)
    
    # 방법2
    new_dict={}
    for blood in blood_types:
        if blood in new_dict:
            continue
        else:
            new_dict[blood]=blood_types.count(blood)
    return new_dict


print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}


# 2. get() 메서드를 사용한 방법
def count_blood_types(blood_types):
    # 방법 1
    # new_dict= dict({'A':0 ,'B':0, 'O':0 , 'AB':0})
    # for k in new_dict.keys():
    #     count= blood_types.count(k)
    #     if new_dict.get(k) ==0:
    #         new_dict.update({k:count})

    # 방법 2
    new_dict ={}
    for blood in blood_types:
        if blood in new_dict:
            new_dict[blood]= new_dict.get(blood,0) +1
        else:
            new_dict[blood]=1
    return new_dict

print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}
