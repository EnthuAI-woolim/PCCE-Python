# 변수

number = 1

print(number)

# 변수를 사용하면 좋은 점
# 1. 값에 의미를 부여한다.
# 2. 코드를 재사용 할 수 있게 한다.
# 3. 유지보수성을 높인다.

welcome_message = "nice to meet you"

print(welcome_message)
print(welcome_message)
print(welcome_message)
print(welcome_message)
print(welcome_message)
print(welcome_message)

# 예약어는 변수명으로 사용할 수 없다.
# True = 1
# print(True)

# 재할당과 동시 할당

name = "kyle" # 할당
print(name) # kyle

name = "alex" # 재할당
print(name) # alex

# ======

# 동시 할당
x, y, z = 1, 2, 3
print(x, y, z)