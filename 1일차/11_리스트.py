# 리스트

# 변수가 하나의 박스라면, 리스트는 여러 개의 박스다!
numbers = [1, 2, 3, 4, 5]
print(numbers)
print(type(numbers))

# 특징1. 리스트는 다양한 자료형을 가질 수 있다.
data = [1, 1.5, "string", True, False]
print(data)
print(type(data))

# 특징2. 빈 리스트 생성 가능하다.
data = []
print(data)
print(type(data))

# 특징3. 여러 내장함수를 통해서 정보를 수집할 수 있다.
numbers = [1, 2, 3, 4, 5]
print(len(numbers)) # 길이 5
print(max(numbers)) # 최댓값 5
print(min(numbers)) # 최솟값 1

# 특징4. 리스트의 덧셈
a = [1, 2]
b = [3, 4]

print(a + b) # [1, 2, 3, 4]
print(b + a) # [3, 4, 1, 2]

a += [5, 6]
print(a) # [1, 2, 5, 6]

# 특징5. 리스트의 곱셈
numbers = [1]
print(numbers * 4) # [1, 1, 1, 1]

numbers = [1, 2, 3]
print(numbers * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 특징6. 인덱싱, 슬라이싱
# 6-1. 인덱싱(indexing)
numbers = [10, 20, 30, 40, 50]

print(numbers[0]) # 10
print(numbers[1]) # 20
print(numbers[2]) # 30
print(numbers[3]) # 40
print(numbers[4]) # 50

print(numbers[-5]) # 10
print(numbers[-4]) # 20
print(numbers[-3]) # 30
print(numbers[-2]) # 40
print(numbers[-1]) # 50

# 6-2. 슬라이싱(Slicing)
numbers = [10, 20, 30, 40, 50]

# 리스트[start:end:step] (step은 생략 가능)
# end는 포함하지 않는다. (start ~ end-1 까지 슬라이싱)

print(numbers[0:2]) # 0~1까지 가져와 [10, 20]
print(numbers[1:4]) # 1~3까지 가져와 [20, 30, 40]
print(numbers[-5:-3]) # -5 ~ -4까지 가져와 [10, 20]
print(numbers[-5:3]) # -5 ~ 2까지 가져와 [10, 20, 30]

# start나 end를 생략하면 맨 처음이거나 맨 끝을 의미한다.
print(numbers[:2]) # 처음 ~ 1까지 가져와 [10, 20]
print(numbers[2:]) # 2 ~ 끝까지 가져와 [30, 40, 50]
print(numbers[:]) # 처음 ~ 끝까지 가져와 [10, 20, 30, 40, 50]

# step을 넣으면 뛰어넘으면서 자른다.
numbers = [10, 20, 30, 40, 50]

print(numbers[0:4]) # [10, 20, 30, 40]
print(numbers[0:4:2]) # [10, 30]
print(numbers[0:4:3]) # [10, 40]
print(numbers[::2]) # [10, 30, 50]

# step은 음수도 가능하다. (양수면 오른쪽, 음수면 왼쪽)
print(numbers[::-1]) # 리스트를 뒤집어라!! [50, 40, 30, 20, 10]