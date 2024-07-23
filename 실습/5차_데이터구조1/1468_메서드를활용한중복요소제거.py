# 아래 함수를 수정하시오.
def remove_duplicates(my_list):
    # new_lst = []
    # for i in list:
    #     same=list.count(i)
    #     if same>1:
    #         for j in range(same-1):
    #             list.remove(i)
    # new_lst.extend(list)

    # return new_lst


    index=0
    new_lst=[]
    while len(my_list)> index:
        same=my_list.count(my_list[index])
        if same >1:
            my_list.remove(my_list[index])
        else:
            index+=1
    new_lst.extend(my_list)
    return new_lst


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)