# 아래 함수를 수정하시오.
def capitalize_words(word):
    list=word.split(' ')
    print(list)
    for i,li in enumerate(list):
        list[i]=li.capitalize()
    return(' '.join(list))


result = capitalize_words("hello, world!")
print(result)
