# 자주 사용하는 내장함수

numbers = [30, 10, 50, 40, 20]

print(len(numbers))  # 길이
print(min(numbers))  # 최솟값
print(max(numbers))  # 최댓값
print(sum(numbers))  # 합계
print(sorted(numbers))  # 정렬(오름차순)
print(sorted(numbers, reverse=True))  # 정렬(내림차순)

# sorted를 사용해서 원하는 조건으로 정렬하기!
# key 옵션을 이용

"""
특정 numbers라는 리스트가 주어진다.
각 원소의 제곱한 값을 기준으로 오름차순으로 정렬하시오.
"""

def square(number):
    return number ** 2

numbers = [-5, -1, 0, 4, 2]

print(sorted(numbers))  # [-5, -1, 0, 2, 4]
print(sorted(numbers, key=square))  # [0, -1, 2, 4, -5]
print(sorted(numbers, key=lambda number: number ** 2))  # [0, -1, 2, 4, -5]

"""
특정 numbers라는 리스트가 주어진다.
각 원소의 제곱한 값을 기준으로 오름차순으로 정렬하시오.
만약에 제곱한 값이 같다면, 크기가 작은 순서대로 정렬하시오.
"""

# 다중 조건 정렬
numbers = [5, -5, 0, -4, 2]
print(sorted(numbers, key=lambda number: number ** 2))  # [0, 2, -4, 5, -5]

def square(number):
    return [number ** 2, number]

print(sorted(numbers, key=square))  # [0, 2, -4, -5, 5]
print(sorted(numbers, key=lambda number: [number ** 2, number]))  # [0, 2, -4, -5, 5]