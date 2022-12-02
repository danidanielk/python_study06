from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring


# 기상청 홈피 -> 맨아래 RSS 클릭 -> 주소선택다하고 나오는 주소 복사 ->

# http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4113158000

# HTTP 통신
hc=HTTPConnection("www.kma.go.kr")

# 위 주소로 요청 GET방식으로. 
hc.request("GET", "/wid/queryDFSRSS.jsp?zone=4113158000")

# 요청에대한 응답 받아오기.
res = hc.getresponse()

# 응답에 대한 내용 가져오기
resBody=res.read()

# 응답에 대한 내용 출력해보기. (알수없는 문자들 나옴)
print(resBody) 

# 한글처리해서 다시 출력해보기  (홈페이지에서 받아온 xml 문서가 그대로 나옴)
print(resBody.decode())

# 이제 파싱해보자.
#    DOM 객체 여러개 찾기:    .iter("태그명")
#    DOM 객체 한개 찾기 :     .find("태그명")

# 가져와서 한글처리한 데이터를 문자화 시켜보자
kmaWeather = fromstring(resBody)

# data 로 나눠진 한덩이씩 가져오기
weathers = kmaWeather.iter("data")
for w in weathers:
    
# 시간 온도 날씨 가져오기.
    print(w.find("hour").text)
    print(w.find("temp").text)
    print(w.find("wfKor").text)