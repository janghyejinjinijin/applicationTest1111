import googletrans
# 구글 트랜스를 불러온다
import pprint

trans = googletrans.Translator()

str1 = "안녕하세요"
#번역할걸 객체인 str1에 넣어본다
str2 = 'i love korea'
#영어도 테스트 되는지 한번 해본다

result1 = trans.translate(str1, dest='en')
#한국어 번역을 돌려본다, dest 번역할 언어를 지정한다// en은 영어버전이라는 뜻이다.
result2 = trans.translate(str1, dest='ko')
result3 = trans.translate(str1, dest='ja')
#pprint.pprint(googletrans.LANGUAGES #번역불러오기
print(f"번역 결과 : {result1.text}")
#f스트링은 사이에 원하는 변수를 삽입할 수 있다.
print(f"번역 결과 : {result2.text}")
print(f"번역 결과 : {result3.text}")