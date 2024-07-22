# 아래 함수를 수정하시오.
def even_elements(my_list):
    arr = []
    index=0
    while len(my_list) > index:
        if my_list[index] %2 ==1:
            my_list.pop(index)
            index=0
        elif my_list[index]%2 !=1:
            index +=1
        else:
            index +=1
    arr.extend(my_list)
    return arr

    # while True:
    #         if len(my_list) > index and my_list[index] %2 ==1:
    #             my_list.pop(index)
    #             index=0
    #             continue
    #         elif len(my_list) > index and my_list[index]%2 !=1:
    #             index +=1
    #         elif  len(my_list) == index:
    #             break
    #         else:
    #             index +=1
    #     arr.extend(my_list)
    #     return arr

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)