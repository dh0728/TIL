import requests
from pprint import pprint as print

dummy_data=[]
for i in range(1,11):
    API_URL = 'https://jsonplaceholder.typicode.com/users/'+str(i)
    response = requests.get(API_URL)
    # JSON -> dict 데이터 변환
    parsed_data = response.json()
    # 특정 데이터 출력
    lat=parsed_data['address']['geo']['lat']
    lng=parsed_data['address']['geo']['lng']
    company=parsed_data['company']['name']
    name= parsed_data['name']
    if float(lat) < 80 and float(lat) > -80 and float(lng) < 80 and float(lng) > -80:
        dummy_data.append({'company':company,'lat':lat,'lng':lng,'name':name})

'''
[{'company': 'Deckow-Crist',
  'lat': '-43.9509',
  'lng': '-34.4618',
  'name': 'Ervin Howell'},
 {'company': 'Romaguera-Jacobson',
  'lat': '-68.6102',
  'lng': '-47.0653',
  'name': 'Clementine Bauch'},
 {'company': 'Keebler LLC',
  'lat': '-31.8129',
  'lng': '62.5342',
  'name': 'Chelsey Dietrich'},
 {'company': 'Considine-Lockman',
  'lat': '-71.4197',
  'lng': '71.7478',
  'name': 'Mrs. Dennis Schulist'},
 {'company': 'Johns Group',
  'lat': '24.8918',
  'lng': '21.8984',
  'name': 'Kurtis Weissnat'},
 {'company': 'Hoeger LLC',
  'lat': '-38.2386',
  'lng': '57.2232',
  'name': 'Clementina DuBuque'}]
'''

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]


def create_user(data):
    censored_user_list={}
    for user in data:
        result =censorship(user)
        if result:
            censored_user_list[user['company']]=[user['name']]
    return censored_user_list

    # print(censored_user_list)

def censorship(user):
    # # print('유저')
    # for index, black in enumerate(black_list):
    #     print(f'{user["company"]}')
    #     print(black)
    if user['company'] in black_list:
        print(f'{user["company"]} 소속의 {user["name"]}은/는 등록할 수 없습니다')
        return False
    else:
        print('이상없습니다.')
        return True


result =create_user(dummy_data)
print(result)
