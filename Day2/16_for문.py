# for 반복문

# 1. 리스트의 반복
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

# 2. 문자열의 반복
word = "python"

for character in word:
    print(character)

# 3. 조건문과 함께 사용 가능하다.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:   # numbers의 수 number에 대해
    if number % 2 == 0:  # number가 짝수면
        print(number)    # 출력

# 4. 레인지(range)와 함께 사용 가능하다.
for i in range(10):  # 0 ~ 9
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)


numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)  # pythonic

for i in range(len(numbers)):
    print(f"{i}번째 원소는 {numbers[i]}")

# enumerate() -> (인덱스, 원소)를 동시에 뽑을 수 있다.
for i, number in enumerate(numbers):
    print(f"{i}번째 원소는 {number}")

"""
0번째 원소는 1
1번째 원소는 2
2번째 원소는 3
3번째 원소는 4
4번째 원소는 5
"""