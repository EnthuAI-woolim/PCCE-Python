# 컨테이너 형 변환

# list()
# 1. 문자열 -> 리스트
name = "kyle"
print(list(name))  # ['k', 'y', 'l', 'e']

# 2. 레인지 -> 리스트
numbers = range(1, 11)  # 1 ~ 10
print(numbers)  # range(1, 11)
print(list(numbers))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
