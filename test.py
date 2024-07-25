import requests
from pprint import pprint
# url ='https://fakestoreapi.com/carts'

# data = requests.get(url).json()

# print(data)

# 서울 위도 37.56 , 경도 126.97
API_Key='10bd323bcd093d0bba8ca5692c33af08'
lat = 37.56 
lon = 126.56

# "TOkyo,JP"
# "New York,US"

city= "Seoul,KR"
url=f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_Key}'
city_url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}'
data = requests.get(city_url).json()

# print(data)
pprint(data)