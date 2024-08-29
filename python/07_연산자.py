# 연산자

# 1. 산술 연산자 -> 사칙연산, 몫, 나머지, 제곱
a = 5
b = 2

print(a + b) # 덧셈
print(a - b) # 뺄셈
print(a * b) # 곱셈
print(a / b) # 나눗셈

print(a // b) # 몫 (나눗셈의 결과가 정수)
print(a % b) # 나머지
print(a ** b) # 제곱


# 2. 복합 연산자
a = 5
b = 2

# 복합 연산자는 자기 자신에게 연산을 할 때만 가능
a += b # a = a + b
a -= b
a *= b
a /= b
a //= b # a = a // b
a %= b
a **= b


# 3. 비교 연산자 => 크다, 작다, 같다, 다르다 ...
# => 참, 거짓 (bool)

print(2 < 5) # 미만 => 참(True)
print(2 <= 5) # 이하
print(2 > 5) # 초과
print(2 >= 5) # 이상

print(2 == 5) # 같다
print(2 != 5) # 다르다

print("one" == "one")
print("one" == "two")


# 4. 논리 연산자 -> bool

# 4-1. and (둘 다 참이여야 참)
print(True and True) # True
print(True and False)
print(False and True)
print(False and False)

# 4-2. or (둘 중 하나라도 참이면 참)
print(True or True)
print(True or False)
print(False or True)
print(False or False) # False

# 4-3. not (반전)
print(not True) # False
print(not False) # True