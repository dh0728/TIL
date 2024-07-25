# 아래에 코드를 작성하시오.
class Myth:
    type_of_myth = 0

    def __init__(self,name):
        self.name = name
        Myth.type_of_myth += 1
    
    @staticmethod
    def description():
        return print(f'신화는 한 나라 혹은 한 민족으로부터 전승되어 오는 예로부터 섬기는 신을 둘러싼 이야기를 뜻한다.')
    
c1 = Myth('dangun')
print(c1.name)
c2 = Myth('greek & rome')
print(c2.name)
num = Myth.type_of_myth
print(f'현재까지 생성된 신화수 : {num}')
Myth.description()
