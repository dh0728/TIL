# 아래 클래스를 수정하시오.
class StringRepeater:
    def __init__(self):
        pass
    @staticmethod
    def repeat_string(num ,word):
        for i in range(num):
            print(word)


repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")


