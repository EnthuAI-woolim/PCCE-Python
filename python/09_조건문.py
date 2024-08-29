# 조건문 (if, else)

"""
if (조건/문장):
    # 조건이 True일 때만 행동한다.
    print("참입니다.")
    print("참입니다.2")
else:
    # 조건이 False일 때만 행동한다.
    print("거짓입니다.")
    print("거짓입니다.2")
"""

if False:
    print("True")
else:
    print("False")

# 비교 연산자와 같이 사용 가능하다.
a = 3

if a < 2:
    print("a는 2보다 작다.")
else:
    print("a는 2보다 작지 않다.")

# 산술 연산자와 혼합해서 사용 가능하다.
number = 5 # 홀수

if number % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

# 논리 연산자도 추가 가능하다.
name = "kyle"
age = 30

# 이름이 kyle이고 나이가 짝수라면,
if name == "kyle" and age % 2 == 0:
    print("안녕하세요~")
else:
    print("처음 뵙겠습니다!")