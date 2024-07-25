# 아래 클래스를 수정하시오.
class UserInfo:
    def __init__(self):
        self.user_data = {}

    def get_user_info(self):
        try:
            self.user_data['name'] = input('이름을 입력하세요 :')
            self.user_data['age'] = int(input('나이를 입력하세요 :'))
        except ValueError:
            print('나이는 숫자로 입력해야 합니다.')           

    def display_user_info(self):
        try:
            self.user_data.get('name')[0] #이름만입력안했을시오류
            print(f'사용자 정보: \n이름: {self.user_data["name"]} \n나이: {self.user_data["age"]}')
        except:
            print('사용자 정보가 입력되지 않았습니다.')


user = UserInfo()
user.get_user_info()
user.display_user_info()

