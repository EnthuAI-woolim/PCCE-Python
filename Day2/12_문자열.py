# 문자열

name = "kyle"
name = 'kyle'

# 특징1. 내장함수를 사용할 수 있다.
print(len(name))  # 길이 - 4

# 특징2. 문자열의 덧셈
a = "1"
b = "2"
print(a + b)  # 12

# 특징3. 문자열의 곱셈
a = "hello"
b = a * 3
print(b)  # hellohellohello

# 특징4. 인덱싱과 슬라이싱
word = "python"

# 4-1. 인덱싱(indexing) - 역시나 음수 인덱싱도 지원!
print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[4])
print(word[5])

print(word[-6])
print(word[-5])
print(word[-4])
print(word[-3])
print(word[-2])
print(word[-1])

# 4-2. 슬라이싱(slicing)
word = "python"

print(word[1:3])  # yt
print(word[:3])  # pyt
print(word[1:])  # ython
print(word[:])  # python
print(word[::-1])  # nohtyp

"""
Palindrome
word가 뒤집었을 때도 같은 모양인가요? -> 팰린드롬을 판별해라!

word = "abba"

if word == word[::-1]:
    print("팰린드롬입니다.")
else:
    print("팰린드롬이 아닙니다.")
"""

# 특징5. 문자열의 삽입과 삭제
# 5-1. 삽입은 안되지만 삽입 된 형태의 새로운 문자열을 만드는 방식으로 가능
word = "python"
word = word + "!"
print(word)  # python!

# 5-2. 삭제도 안되지만 삭제 된 형태의 새로운 문자열을 만드는 방식으로 가능
word = "python"
word = word[:2] + word[3:]
print(word)  # pyhon

# 특징6. 문자열의 포매팅(formatting)
name = "alex"
print("제 이름은 " + name + "입니다.")  # 제 이름은 alex입니다.

# f-string
# 1. 맨 앞에 f 키워드를 붙여야 한다.
# 2. 변수를 중괄호로 감싸야 한다.
name = "kyle"
print(f"제 이름은 {name}입니다.")  # 제 이름은 kyle입니다.

name = "kyle"
age = 30
print(f"제 이름은 {name}이고, 나이는 {age + 5}세 입니다.")  # 제 이름은 kyle이고, 나이는 30세 입니다.
print(f"제 이름은 {name}이고, 이름의 길이는 {len(name)}입니다.")  # 제 이름은 kyle이고, 이름의 길이는 4입니다.