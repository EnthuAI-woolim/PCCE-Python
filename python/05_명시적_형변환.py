# 명시적 형변환

# 1. int() => "다른 자료형 -> 정수"
print(int("123"))
print(type(int("123")))

print(int(1.2)) # -> 소수점이 없어짐(버림)
print(int(3.145))

print(int(True)) # 1
print(int(False)) # 0

# 2. float() => "다른 자료형 -> 실수"
print(float(30))
print(type(float(30)))

print(float("3.5"))
print(type(float("3.5")))

# print(float("hello")) # 형식에 맞는 문자열을 넣어야함

# 3. str() -> "다른 자료형 -> 문자열"
print(str(123))
print(str(1.23))

print(type(str(123)))
print(type(str(1.23)))

# 4. bool() -> "다른 자료형 -> 불린형"

# True로 평가되는 것들
print(bool(1))
print(bool(1.2))
print(bool("hello"))
print(bool([1, 2, 3]))

# False로 평가되는 것들
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool([]))