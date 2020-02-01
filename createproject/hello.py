import requests #=download받은 함수들을 가지고온 것
from bs4 import BeautifulSoup #=다운받은 함수 중 beautifulsoup만 가져온다는 뜻.

#headers: 크롤링은 기기에서 자동으로 클릭하는게 아니어서 user agent가 비어있음. so user agent를 넣어서 실제로 사람이 접속하는 거라고 넣어주는 것.
#파싱: 데이터(문자열)를 사용자가 사용하기 용이한 형태(예:html)로 바꿔주는 기능
# 타겟 URL을 읽어서 HTML를 받아오고,


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20190909', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')
print(soup)
#############################
# (입맛에 맞게 코딩)
#############################


import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20190909',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기 (tr: table row)
movies = soup.select('#old_content > table > tbody > tr')
#false=0=none='' 조건문에서 동일함
#true=1='asbsad'=1230=[1,2,3] 비어있지 않은 것은 true
# movies (tr들) 의 반복문을 돌리기
for movie in movies:
    # movie 안에 a 가 있으면,
    a_tag = movie.select_one('td.title > div > a')
    if a_tag is not None:
        # a의 text를 찍어본다.
        print (a_tag.text)

