def count_character(word, exam):
    count=word.count(exam)
    return count
    

result = count_character("Hello, World!", "o")
print(result)  # 2
