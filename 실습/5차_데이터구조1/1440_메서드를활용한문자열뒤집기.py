# 아래 함수를 수정하시오.
def reverse_string(word):
    #리스트활용
    # arr=[]
    # arr.extend(word)
    # arr.reverse()
    revsered_word=reversed(word)
    result =''.join(revsered_word)
    return result


result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH
