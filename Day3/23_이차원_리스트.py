# 이차원 리스트

# 1. 이중 for 문
# for a in range(4):
#     print(f"a가 {a}일 때 : ")

#     for b in range(4):
#         print(f"b가 {b}이다.")

# 2. 이차원 리스트
# 행렬(Matrix)이라고도 한다.
# 단순히 리스트 안에 리스트가 있는거다.

numbers = [1, 2, 3, 4]  # 일차원 리스트 - 선
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 이차원 리스트 - 면

matrix = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]

# 2-1. 이차원 리스트의 인덱싱
matrix = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]

print(matrix[0])  # [1, 2, 3]
print(matrix[0][0])  # 1
print(matrix[0][1])  # 2
print(matrix[2][2])  # 9

# 2-2. 이차원 리스트의 수정
numbers = [1, 2, 3]
numbers[0] = 4
print(numbers)  # [4, 2, 3]

matrix = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]

matrix[0][0] = 4
print(matrix)  # [[4, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix[0] = []
print(matrix)  # [[], [4, 5, 6], [7, 8, 9]]

# 2-3. 이차원 리스트의 순회
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
]

print(matrix)  # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]]

"""
1 2 3 4
5 6 7 8
9 0 1 2
"""

print(matrix[0][0], matrix[0][1], matrix[0][2], matrix[0][3])
print(matrix[1][0], matrix[1][1], matrix[1][2], matrix[1][3])
print(matrix[2][0], matrix[2][1], matrix[2][2], matrix[2][3])


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
]

# 이중 for문을 이용해서 순회 가능
for i in range(3):  # 3행
    for j in range(4):  # 4행
        print(matrix[i][j], end=" ")

    print()

"""
행순회
1 2 3 4 
5 6 7 8 
9 0 1 2

열순회
1 5 9
2 6 0
3 7 1
4 8 2
"""