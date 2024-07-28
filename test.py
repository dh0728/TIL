import requests
from pprint import pprint

URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

def get_bestseller_books():
    A = [
        {'title': '죄와벌' ,'salesPoint': 3},
        {'title': '베니스' ,'salesPoint': 5},
        {'title': '아아아' ,'salesPoint': 2},
        {'title': '춘향전' ,'salesPoint': 4},
        {'title': '호구와트' ,'salesPoint': 1},
        ]
    B = []
    C = []

    #sort를 활용한 정렬 
    sorted_A = sorted(A, key=lambda x: x['salesPoint'],reverse=True)
    print(sorted_A)
    
    sorted_B = sorted(A, key=lambda x: x['title'], reverse=True)
    print(sorted_B)
    
    for i in A:
        B.append(i['salesPoint'])
        C.append(i['title'])
        # D = dict(zip(C, B))
    
    # c =sorted(A)
    # print(c)
    # print(B)
    E = []
    for j in range(len(B)):
        E.append({'제목': C[j], '판매지수': B[j]})


    return E

result= get_bestseller_books()
# print(result)