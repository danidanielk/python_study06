# 네이버 개발자센터 접속 -> 로그인 -> document -> 검색 -> 쇼핑 -> url 복사
from http.client import HTTPSConnection
from urllib.parse import quote
from xml.etree.ElementTree import fromstring

# https://openapi.naver.com/v1/search/shop.xml

# 상품명 :입력
# xml파싱해서
# 문서의 제목 / 최저가 / 브랜드 / 대분류 / 카테고리 정보를 출력.
# 3BqyvggEPRKNT4VKFEzQ
# HgiC5z870R
q=input("검색: ")
q=quote(q) #urllib.parse << 로 임포트  (검색어를 기계어?로변환)

#https 통신 
hc=HTTPSConnection("openapi.naver.com")

#필수 요청파라미터 query 를 써주라함. 시작을 알리는 ?먼저써주고query= 붙혀주고 + 검색어
#아이디랑 비번도 헤더에 필수로 넣으라함 요청해더처리 (딕트형태로)
h={
    "X-Naver-Client-Id":"3BqyvggEPRKNT4VKFEzQ",
    "X-Naver-Client-Secret" : "HgiC5z870R"
    }
hc.request("GET", "/v1/search/shop.xml?query="+q,headers=h)

#응답 받아서 읽어오기 한줄로
resBody=hc.getresponse().read()
print(resBody.decode())

#한줄로 결과물이 나오는데 보기 불편하니 xml파일 만들어 붙여넣어주자.
#덩어리가 아이템으로 나뉘어있다 반복문 돌려보자.
#DOM객체 여러개 찾기 .iter("태그명")
#DOM객체 한개만 찾기 .find("태그명")

#타이틀에 있는 b태그 없애는 함수만들어서 아래 반복문 타이틀쪽에 감싸기
def cut(text):
    text=text.replace("<b>","")
    text=text.replace("</b>","")
    return text

#XML은 Fromstring 로 변환해서 받아온다.
#Json은 loads로 
for p in fromstring(resBody).iter("item"):
    print(cut(p.find("title").text))
    print(p.find("lprice").text)
    print(p.find("brand").text)
    print(p.find("category1").text)
    print("-----------")