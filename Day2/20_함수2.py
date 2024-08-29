# 함수(function)

"""
[함수의 네 가지 형태]

1. 매개변수 O, 반환값 O
2. 매개변수 O, 반환값 X
3. 매개변수 X, 반환값 O
4. 매개변수 X, 반환값 X
"""

# 1. 매개변수 O, 반환값 O
def add(x, y):
    return x + y

result = add(1, 2)
print(result)  # 3

# 2. 매개변수 O, 반환값 X -> None을 반환한다
def hello(name):
    print(f"{name}님 안녕하세요!")

hello("kyle")

# 3. 매개변수 X, 반환값 O -> 반환값이 고정된다
# "고정적으로 정해진 동작만 수행해서 그 결과를 받겠다."
def get_even_numbers_from_one_to_ten():
    result = []

    for i in range(1, 11):
        if i % 2 == 0:
            result.append(i)
    
    return result

result = get_even_numbers_from_one_to_ten()
print(result)  # [2, 4, 6, 8, 10]

# 4. 매개변수 X, 반환값 X
# "고정적으로 정해진 동작만 수행한다."
def welcome():
    print("Welcome to Python!")
    print("Welcome to Python!")
    print("Welcome to Python!")
    print("Welcome to Python!")
    print("Welcome to Python!")

welcome()


"""
람다 표현식(Lambda Expression)
-> 함수를 간단하게 한 줄로 표현 할 수 있다!

"lambda 매개변수: 표현식"
"""

# 람다 적용 전
def add(x, y):
    return x + y

result = add(1, 2)
print(result)  # 3

# 람다 적용 후
add = lambda x, y: x + y
result = add(1, 2)
print(result)  # 3

# 함수는 일급 객체(First Class Object)이기 때문에 람다가 가능하다.
# 일급 객체의 세 가지 특징
# 1. 변수에 할당할 수 있다.
def add(x, y):
    return x + y

another_add = add
print(add(3, 4))  # 7
print(another_add(3, 4))  # 7

# 2. 매개변수로 전달할 수 있다.
def add(x, y):
    return x + y

def add_numbers(func, x, y):
    return func(x, y)

result = add_numbers(add, 1, 2)
print(result)  # 3


# 3. 반환값으로 사용될 수 있다.
def add(x, y):
    return x + y

def get_add_func():
    return add

result = get_add_func()(5, 6)
print(result)  # 11