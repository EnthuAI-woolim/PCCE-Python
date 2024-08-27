# break, continue

# 1. break -> 반복문 탈출하기
# 1-1. for break
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

    if number == 4:
        break

# 1-2. break 사용 예시
names = ["kyle", "alex", "harry", "justin", "haley", "ken", "beemo"]

for i, name in enumerate(names):
    if name == "harry":
        print(i)  # 2
        break

# 1-3. while break
numbers = [1, 2, 3, 4, 5]
i = 0

while i < len(numbers):
    print(numbers[i])

    if numbers[i] == 4:
        break
    
    i += 1


# 2. continue -> 반복을 하다가 만나면, 그 다음 반복으로 넘어가라.
# 2-1. for continue
numbers = [1, 2, 3, 4, 5]

# 홀수만 출력해라 == 짝수는 넘어가라
for number in numbers:
    if number % 2 == 0:
        continue
    
    print(number)

"""
for number in numbers:
    if number % 2 == 1:
        print(number)
"""

# 2-2. while continue
numbers = [1, 2, 3, 4, 5]
i = 0

while i < len(numbers):
    if numbers[i] % 2 == 0:
        i += 1  # while에서 continue를 사용할 때는 항상 증감식을 주의한다!
        continue

    print(numbers[i])
    i += 1