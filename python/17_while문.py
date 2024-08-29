# while 반복문

# 순서
# 1. 초기화를 해준다.
# 2. 조건문을 작성한다.
# 3. 증감식을 작성한다.

for i in range(6):  # 0 ~ 5 를 출력
    print(i)

i = 0
while i <= 5:  # 0 ~ 5 를 출력
    print(i)
    i += 1

# 리스트나 문자열과 같은 컨테이너와 함께 사용 가능
numbers = [10, 20, 30, 40, 50]

i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1

# while도 if와 함께 사용이 가능
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0

while i < len(numbers):
    if numbers[i] % 2 == 0:
        print(numbers[i])
    i += 1  # 들여쓰기 주의