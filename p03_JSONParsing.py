#JSON 파싱
# 구글 -> openweathermap 검색 -> Current weather data -> Built-in API request by city name -> 첫번째 API 긁어옴..
from urllib.parse import quote
from http.client import HTTPSConnection
from json import loads

# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

# 쌤 key = 42008a8c8e7402a3fc9d3b1a7df8fee9

# 도시 이름을 입력 : (해외사이트기때문에 영어로) 
# 응답 내용 출력.

q=input("검색: ")
q=quote(q)

hc=HTTPSConnection("api.openweathermap.org")
#뒤에 &lang=kr 추가  한국어번역
hc.request("GET", "/data/2.5/weather?q="+q+"&appid=42008a8c8e7402a3fc9d3b1a7df8fee9&lang=kr")
resBody=hc.getresponse().read()
#print로 받아와서 file생성 > .xml 로 만들고 붙여넣고  print는 다시 주석처리
#print(resBody.decode())

#Json 에서는 loads (import json __init__
weatherData = loads(resBody) #JAVASCRIPT - > Python으로 변경


#데이터를 Dict/ list 확인하면서콘솔창에 출력.
print(weatherData["weather"][0]["description"])
print(weatherData["main"]["temp"])
print(weatherData["main"]["feels_like"])
print(weatherData["main"]["humidity"])
print(weatherData["wind"]["speed"])