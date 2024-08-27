# 함수(function)

"""
기본구조

def 함수명(매개변수1, 매개변수2, 매개변수3 ....):
    동작1
    동작2

    return 반환값
"""

# 1. 함수의 선언(define)
def add(x, y):
    result = x + y

    return result

# 2. 함수의 호출(call)
print(add(1, 2))  # 3

result = add(1, 2)
print(result)  # 3

# 3. 함수를 사용하는 이유
# 3-1. 만약에 함수가 없다면
a = 5
b = 10

if a > b:
    bigger = a
else:
    bigger = b

print(bigger)  # 10 -> b

c = 6
d = 3

if c > d:
    bigger = c
else:
    bigger = d

print(bigger)  # 6 -> c

# 3-2. 함수를 사용해서 재사용성을 높인다.
def compare(x, y):
    if x > y:
        return x
    else:
        return y

a = 5
b = 10
print(compare(a, b))  # 10 -> b

c = 6
d = 3
print(compare(c, d))  # 6 -> c
